import customtkinter as ctk
from tkinter import messagebox, ttk, filedialog
import pymysql
import pandas as pd
import os, bcrypt
from PIL import Image

#Colores diseño nuevo
COLOR_FONDO = "white"  
COLOR_FRAME = "white"  
COLOR_BOTON = "#058A15"  
COLOR_BOTON_HOVER = "green"  
COLOR_TEXTO = "black"
pantalla=None

# Clase para manejar la base de datos
class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="contrataciones"
        )
        self.cursor = self.connection.cursor()

    def ejecutar_consulta(self, consulta, valores=None):
        try:
            if valores:
                self.cursor.execute(consulta, valores)
            else:
                self.cursor.execute(consulta)
            self.connection.commit()
        except Exception as e:
            messagebox.showerror("Error en consulta", f"{e}")
            raise  # Lanzar la excepción para detener la ejecución

    def obtener_datos(self, consulta):
        try:
            self.cursor.execute(consulta)
            return self.cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error en consulta", f"{e}")
            return []

    def __del__(self):
        self.cursor.close()
        self.connection.close()


# Variables globales
usuario_iniciado = True  # Cambia a False si el usuario aún no ha iniciado sesión
menu_expandido = False
db = DataBase()  # Instancia de la base de datos

def abrir_pantalla(contenido_frame, titulo):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    
    fuente = ctk.CTkFont(family="Zurich.ttf", weight="bold", size=25)
    label_titulo = ctk.CTkLabel(contenido_frame, text=titulo, font=fuente, text_color="#446344")
    label_titulo.pack(pady=20)
    
    funciones_pantalla = {
        "Pantalla ARL": mostrar_arl,
        "Pantalla EPS": lambda frame: mostrar_eps(frame, db),
        "Pantalla Bancos": mostrar_bancos,
        "Pantalla Ciudad": mostrar_ciudad,
        "Pantalla Cargo": mostrar_cargo,
        "Pantalla Tipo de contrato": mostrar_tipodecontrato,
        "Pantalla Dependencia": mostrar_dependencia,
        "Pantalla Departamento": mostrar_departamento,
        "Pantalla RH": mostrar_rh,
        "Pantalla Género": mostrar_genero,
        "Pantalla Tipo de documento": mostrar_tipodedocumento,
        "Pantalla Tipo de Cuenta": mostrar_tipo_cuenta,
        "Pantalla Contrato": mostrar_contrato,
        "Pantalla Contratistas": mostrar_Contratista,
        "Pantalla Jefe": mostrar_jefes,
        "Pantalla Registro Usuarios": mostrar_usuario
    }
    
    if titulo in funciones_pantalla:
        funciones_pantalla[titulo](contenido_frame)

# Función para mostrar la pantalla de EPS
def mostrar_eps(frame, db):
    modificar = False
    dni = ctk.StringVar()
    nombre = ctk.StringVar()

    def exportar_a_excel_eps():
        try:
            sql = "SELECT id, nombreEPS FROM eps"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            if filas:
                df = pd.DataFrame(filas, columns=['ID', 'Nombre'])
                filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                        filetypes=[("Excel files", "*.xlsx"),
                                                                   ("All files", "*.*")])
                if filepath:
                    df.to_excel(filepath, index=False)
                    messagebox.showinfo("Exportación Exitosa", f"Datos exportados a {filepath}")
                    os.startfile(filepath)
            else:
                messagebox.showwarning("Sin Datos", "No hay datos para exportar")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar los datos: {e}")

    def importar_de_excel_eps():
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath:
            try:
                df = pd.read_excel(filepath)
                for _, row in df.iterrows():
                    sql = "INSERT INTO eps (id, nombreEPS) VALUES (%s, %s)"
                    db.cursor.execute(sql, (row['ID'], row['Nombre']))
                db.connection.commit()
                messagebox.showinfo("Importación Exitosa", "Datos importados correctamente desde Excel")
                llenar_tabla()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo importar los datos: {e}")

    def seleccionar(event):
        seleccion = tveps.selection()
        if seleccion:
            id = seleccion[0]
            valores = tveps.item(id, "values")
            dni.set(valores[0])
            nombre.set(valores[1])

    marco = ctk.CTkFrame(frame, fg_color="transparent")
    marco.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(marco, text="DNI",text_color=COLOR_TEXTO).grid(column=0, row=0, padx=5, pady=5)
    txtDni = ctk.CTkEntry(marco, textvariable=dni,fg_color="white")
    txtDni.grid(column=1, row=0)

    ctk.CTkLabel(marco, text="Nombre",text_color=COLOR_TEXTO).grid(column=0, row=1, padx=5, pady=5)
    txtNombre = ctk.CTkEntry(marco, textvariable=nombre,fg_color="white")
    txtNombre.grid(column=1, row=1)

    lblMensaje = ctk.CTkLabel(marco, text="Aquí van los mensajes", fg_color="green")
    lblMensaje.grid(column=0, row=2, columnspan=4)

    tveps = ttk.Treeview(marco, selectmode='none')
    tveps["columns"] = ("DNI", "Nombre")
    tveps.column("#0", width=0, stretch='no')
    tveps.column("DNI", width=150, anchor='center')
    tveps.column("Nombre", width=150, anchor='center')
    tveps.heading("#0", text="")
    tveps.heading("DNI", text="DNI", anchor='center')
    tveps.heading("Nombre", text="Nombre", anchor='center')
    tveps.grid(column=0, row=3, columnspan=4, padx=5)
    tveps.bind("<<TreeviewSelect>>", seleccionar)

    btnEliminar = ctk.CTkButton(marco, text="Eliminar", command=lambda: eliminar(), fg_color=COLOR_BOTON)
    btnEliminar.grid(column=1, row=4)
    btnNuevo = ctk.CTkButton(marco, text="Guardar", command=lambda: nuevo(), fg_color=COLOR_BOTON)
    btnNuevo.grid(column=2, row=4)
    btnModificar = ctk.CTkButton(marco, text="Seleccionar", command=lambda: actualizar(), fg_color=COLOR_BOTON)
    btnModificar.grid(column=3, row=4)

    btnExportar = ctk.CTkButton(marco, text="Exportar a Excel", command=exportar_a_excel_eps, fg_color=COLOR_BOTON)
    btnExportar.grid(column=2, row=5, pady=10)
    btnImportar = ctk.CTkButton(marco, text="Importar de Excel", command=importar_de_excel_eps, fg_color=COLOR_BOTON)
    btnImportar.grid(column=3, row=5, pady=10)

    def modificarFalse():
        nonlocal modificar
        modificar = False
        tveps.config(selectmode='none')
        btnNuevo.configure(text="Guardar")
        btnModificar.configure(text="Seleccionar")
        btnEliminar.configure(state='disabled')

    def modificarTrue():
        nonlocal modificar
        modificar = True
        tveps.config(selectmode='browse')
        btnNuevo.configure(text="Nuevo")
        btnModificar.configure(text="Modificar")
        btnEliminar.configure(state='normal')

    def validar():
        return len(dni.get()) > 0 and len(nombre.get()) > 0

    def limpiar():
        dni.set("")
        nombre.set("")

    def vaciar_tabla():
        for fila in tveps.get_children():
            tveps.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        sql = "SELECT id, nombreEPS FROM eps"
        db.cursor.execute(sql)
        filas = db.cursor.fetchall()
        for fila in filas:
            tveps.insert("", 'end', str(fila[0]), text=str(fila[0]), values=(fila[0], fila[1]))

    def eliminar():
        seleccion = tveps.selection()
        if seleccion:
            id_real = tveps.item(seleccion[0], "values")[0]
            sql = "DELETE FROM eps WHERE id=%s"
            db.cursor.execute(sql, (id_real,))
            db.connection.commit()
            tveps.delete(seleccion[0])
            lblMensaje.configure(text="Registro eliminado correctamente", fg_color="green")
            limpiar()

    def nuevo():
        if not modificar:
            if validar():
                sql = "INSERT INTO eps (id, nombreEPS) VALUES (%s, %s)"
                db.cursor.execute(sql, (dni.get(), nombre.get()))
                db.connection.commit()
                lblMensaje.configure(text="Registro guardado con éxito", fg_color="green")
                llenar_tabla()
                limpiar()
            else:
                lblMensaje.configure(text="Los campos no deben estar vacíos", fg_color="red")
        else:
            modificarFalse()

    def actualizar():
        if modificar:
            if validar():
                seleccion = tveps.selection()
                if seleccion:
                    id_real = tveps.item(seleccion[0], "values")[0]
                    sql = "UPDATE eps SET nombreEPS=%s WHERE id=%s"
                    db.cursor.execute(sql, (nombre.get(), id_real))
                    db.connection.commit()
                    lblMensaje.configure(text="Registro actualizado con éxito", fg_color="green")
                    llenar_tabla()
                    limpiar()
            else:
                lblMensaje.configure(text="Los campos no deben estar vacíos", fg_color="red")
        else:
            modificarTrue()

    # Llenar la tabla cuando se abra la ventana
    llenar_tabla()

# Función para mostrar ARL
def mostrar_arl(frame):
    db = DataBase()
    dni = ctk.StringVar()
    nombre = ctk.StringVar()

    def seleccionar(event):
        seleccion = tvEstudiantes.selection()
        if seleccion:
            valores = tvEstudiantes.item(seleccion[0], "values")
            dni.set(valores[0])
            nombre.set(valores[1])

    def limpiar():
        dni.set("")
        nombre.set("")

    def llenar_tabla():
        tvEstudiantes.delete(*tvEstudiantes.get_children())
        for fila in db.obtener_datos("SELECT id, nombreARL FROM arl"):
            tvEstudiantes.insert("", "end", values=fila)

    def nuevo():
        if dni.get() and nombre.get():
            db.ejecutar_consulta("INSERT INTO arl (id, nombreARL) VALUES (%s, %s)", (dni.get(), nombre.get()))
            llenar_tabla()
            limpiar()

    def eliminar():
        seleccion = tvEstudiantes.selection()
        if seleccion:
            id_seleccionado = tvEstudiantes.item(seleccion[0], "values")[0]
            db.ejecutar_consulta("DELETE FROM arl WHERE id=%s", (id_seleccionado,))
            llenar_tabla()

    def exportar_a_excel_arl():
        try:
            filas = db.obtener_datos("SELECT id, nombreARL FROM arl")
            if filas:
                filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
                if filepath:
                    pd.DataFrame(filas, columns=['ID', 'Nombre']).to_excel(filepath, index=False)
                    messagebox.showinfo("Exportación Exitosa", f"Datos exportados a {filepath}")
            else:
                messagebox.showwarning("Sin Datos", "No hay datos para exportar")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante la exportación: {e}")

    def importar_desde_excel_arl():
        try:
            filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
            if filepath:
                df = pd.read_excel(filepath)
                if "ID" in df.columns and "Nombre" in df.columns:
                    for _, row in df.iterrows():
                        if not db.obtener_datos(f"SELECT id FROM arl WHERE id = {row['ID']}"):
                            db.ejecutar_consulta("INSERT INTO arl (id, nombreARL) VALUES (%s, %s)", (row["ID"], row["Nombre"]))
                    messagebox.showinfo("Importación Exitosa", "Datos importados correctamente")
                else:
                    messagebox.showerror("Error", "Formato incorrecto en el archivo")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante la importación: {e}")

    # Marco para el contenido principal
    contenido_marco = ctk.CTkFrame(frame, fg_color="transparent")
    contenido_marco.pack(fill="both", expand=True, padx=20, pady=20)

    # UI del formulario ARL
    ctk.CTkLabel(contenido_marco, text="DNI",text_color=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ctk.CTkEntry(contenido_marco, textvariable=dni,fg_color="white", text_color=COLOR_TEXTO).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(contenido_marco, text="Nombre",text_color=COLOR_TEXTO).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    ctk.CTkEntry(contenido_marco, textvariable=nombre,fg_color="white", text_color=COLOR_TEXTO).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkButton(contenido_marco, text="Guardar", command=nuevo, fg_color=COLOR_BOTON).grid(row=2, column=0, pady=10, sticky="ew")
    ctk.CTkButton(contenido_marco, text="Eliminar", command=eliminar,fg_color=COLOR_BOTON).grid(row=2, column=1, pady=10, sticky="ew")

    # Botón para cerrar la ventana de ARL
    ctk.CTkButton(contenido_marco, text="Cerrar", command=frame.destroy, fg_color=COLOR_BOTON).grid(row=2, column=2, pady=10, padx=10, sticky="ew")

    tvEstudiantes = ttk.Treeview(contenido_marco, columns=("DNI", "Nombre"), show="headings")
    tvEstudiantes.heading("DNI", text="DNI")
    tvEstudiantes.heading("Nombre", text="Nombre")
    tvEstudiantes.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
    tvEstudiantes.bind("<<TreeviewSelect>>", seleccionar)

    # Configurar la expansión de la fila del Treeview
    contenido_marco.grid_rowconfigure(3, weight=1)
    contenido_marco.grid_columnconfigure(1, weight=1)

    # Botones de exportar e importar
    ctk.CTkButton(contenido_marco, text="Exportar a Excel", command=exportar_a_excel_arl, fg_color=COLOR_BOTON).grid(row=4, column=0, pady=10, sticky="ew")
    ctk.CTkButton(contenido_marco, text="Importar desde Excel", command=importar_desde_excel_arl, fg_color=COLOR_BOTON).grid(row=4, column=1, pady=10, sticky="ew")

    llenar_tabla()

# Funciones vacías para otras pantallas 
def mostrar_bancos(frame):
    pass
def mostrar_bancos(frame):
    global db, modificar, page_number, records_per_page
    db = DataBase()
    modificar = False
    page_number = 1
    records_per_page = 10

    # Variables de filtro y registro
    banco_seleccionado = ctk.StringVar()
    tipo_cuenta_seleccionada = ctk.StringVar()
    dni = ctk.StringVar()
    nombre = ctk.StringVar()
    tipoCuenta = ctk.StringVar()

    # Función para seleccionar elementos de la tabla
    def seleccionar(event):
        seleccion = tvBancos.selection()
        if seleccion:
            id = seleccion[0]
            valores = tvBancos.item(id, "values")
            dni.set(valores[0])
            nombre.set(valores[1])
            tipoCuenta.set(valores[2])
            txtID.configure(state='disabled')

    # Función para cargar los datos de tipo de cuenta y bancos
    def cargar_tipo_cuenta():
        try:
            db.cursor.execute("SELECT nombreTipoCuenta FROM tipodecuenta")
            return [fila[0] for fila in db.cursor.fetchall()]
        except Exception as e:
            print(f"Error al cargar los tipos de cuenta: {e}")
            return []

    def cargar_bancos():
        try:
            db.cursor.execute("SELECT DISTINCT nombreBanco FROM banco")
            return [fila[0] for fila in db.cursor.fetchall()]
        except Exception as e:
            print(f"Error al cargar los bancos: {e}")
            return []

    # Función para vaciar la tabla
    def vaciar_tabla():
        for fila in tvBancos.get_children():
            tvBancos.delete(fila)

    # Función para llenar la tabla con datos
    def llenar_tabla(filtro_banco=None, filtro_tipo_cuenta=None):
        vaciar_tabla()
        try:
            offset = (page_number - 1) * records_per_page
            sql = """
            SELECT b.id, b.nombreBanco, tc.nombreTipoCuenta
            FROM banco b
            JOIN tipodecuenta tc ON b.tipoCuenta = tc.id
            """
            params = []
            if filtro_banco:
                sql += " WHERE b.nombreBanco = %s"
                params.append(filtro_banco)
            if filtro_tipo_cuenta:
                sql += " AND tc.nombreTipoCuenta = %s" if filtro_banco else " WHERE tc.nombreTipoCuenta = %s"
                params.append(filtro_tipo_cuenta)
            sql += " LIMIT %s OFFSET %s"
            params.extend([records_per_page, offset])
            db.cursor.execute(sql, tuple(params))
            for fila in db.cursor.fetchall():
                tvBancos.insert("", 'end', fila[0], text=fila[0], values=(fila[0], fila[1], fila[2]))
        except Exception as e:
            print(f"Error al llenar la tabla: {e}")

    def filtrar_registros():
        llenar_tabla(banco_seleccionado.get(), tipo_cuenta_seleccionada.get())

    def mostrar_todos():
        banco_seleccionado.set("")
        tipo_cuenta_seleccionada.set("")
        llenar_tabla()

    def limpiar():
        dni.set("")
        nombre.set("")
        tipoCuenta.set("")
        txtID.configure(state='normal')

    def eliminar():
        seleccion = tvBancos.selection()
        if seleccion:
            try:
                id = seleccion[0]
                db.cursor.execute("DELETE FROM banco WHERE id=%s", (id,))
                db.connection.commit()
                lblMensaje.configure(text="Se ha eliminado el registro correctamente", fg_color="green")
                llenar_tabla()
                limpiar()
            except Exception as e:
                print(f"Error al eliminar: {e}")
                lblMensaje.configure(text="Error al eliminar el registro.", fg_color="red")
        else:
            lblMensaje.configure(text="Seleccione un registro para eliminar", fg_color="red")

    # Crear un nuevo marco para la sección de Bancos
    for widget in frame.winfo_children():
        widget.destroy()
    
    marco_bancos = ctk.CTkFrame(frame, fg_color="transparent")
    marco_bancos.pack(fill="both", expand=True, padx=20, pady=20)

    # Widgets dentro del marco
    ctk.CTkLabel(marco_bancos, text="ID Banco", text_color=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    txtID = ctk.CTkEntry(marco_bancos, textvariable=dni, fg_color="white", text_color=COLOR_TEXTO)
    txtID.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    lblMensaje = ctk.CTkLabel(marco_bancos, text="", fg_color="transparent", text_color=COLOR_TEXTO)
    lblMensaje.grid(row=3, column=0, columnspan=2, pady=10)

    btnEliminar = ctk.CTkButton(marco_bancos, text="Eliminar", command=eliminar, fg_color=COLOR_BOTON)
    btnEliminar.grid(row=5, column=0, pady=10, sticky="ew")

    # Treeview con encabezados
    tvBancos = ttk.Treeview(marco_bancos, columns=("ID", "Nombre", "Tipo de Cuenta"), show="headings")
    tvBancos.heading("ID", text="ID")
    tvBancos.heading("Nombre", text="Nombre")
    tvBancos.heading("Tipo de Cuenta", text="Tipo de Cuenta")
    tvBancos.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    tvBancos.bind("<<TreeviewSelect>>", seleccionar)

    # Configurar expansión de la tabla
    marco_bancos.grid_rowconfigure(9, weight=1)
    marco_bancos.grid_columnconfigure(1, weight=1)

    llenar_tabla()


def mostrar_ciudad(frame):
    pass


def mostrar_ciudad(frame):
    global db, page_number, records_per_page, total_records
    db = DataBase()
    modificar = False
    dni = ctk.StringVar()
    nombre = ctk.StringVar()
    filtro_id = ctk.StringVar()
    filtro_nombre = ctk.StringVar()

    # Inicializar variables de paginación
    page_number = 1
    records_per_page = 10
    total_records = 0

    def seleccionar(event):
        seleccion = tvciudad.selection()
        if seleccion:
            id = seleccion[0]
            valores = tvciudad.item(id, "values")
            dni.set(valores[0])
            nombre.set(valores[1])

    def vaciar_tabla():
        filas = tvciudad.get_children()
        for fila in filas:
            tvciudad.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        global total_records
        offset = (page_number - 1) * records_per_page
        try:
            sql_count = "SELECT COUNT(*) FROM ciudad WHERE 1=1"
            sql = "SELECT id, nombreCiudad FROM ciudad WHERE 1=1"
            parametros = []

            if filtro_id.get():
                sql_count += " AND id LIKE %s"
                sql += " AND id LIKE %s"
                parametros.append(f"%{filtro_id.get()}%")

            if filtro_nombre.get():
                sql_count += " AND nombreCiudad LIKE %s"
                sql += " AND nombreCiudad LIKE %s"
                parametros.append(f"%{filtro_nombre.get()}%")

            db.cursor.execute(sql_count, tuple(parametros))
            total_records = db.cursor.fetchone()[0]

            sql += " LIMIT %s OFFSET %s"
            parametros.extend([records_per_page, offset])
            db.cursor.execute(sql, tuple(parametros))
            filas = db.cursor.fetchall()

            for fila in filas:
                tvciudad.insert("", 'end', iid=fila[0], text=fila[0], values=(fila[0], fila[1]))

            btnPrev.configure(state='normal' if page_number > 1 else 'disabled')
            btnNext.configure(state='normal' if page_number * records_per_page < total_records else 'disabled')
        except Exception as e:
            lblMensaje.configure(text=f"Error al llenar la tabla: {e}", fg_color="red")

    def validar():
        return len(nombre.get()) > 0

    def prev_page():
        global page_number
        if page_number > 1:
            page_number -= 1
            llenar_tabla()

    def next_page():
        global page_number
        if page_number * records_per_page < total_records:
            page_number += 1
            llenar_tabla()

    def limpiar():
        dni.set("")
        nombre.set("")

    def eliminar():
        seleccion = tvciudad.selection()
        if seleccion:
            id = seleccion[0]
            sql = "DELETE FROM ciudad WHERE id=%s"
            db.cursor.execute(sql, (id,))
            db.connection.commit()
            tvciudad.delete(id)
            lblMensaje.configure(text="Registro eliminado", fg_color="green")
            limpiar()
            llenar_tabla()
        else:
            lblMensaje.configure(text="Seleccione un registro para eliminar", fg_color="red")

    def nuevo():
        if validar():
            val = (nombre.get(),)
            sql = "INSERT INTO ciudad (nombreCiudad) VALUES (%s)"
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMensaje.configure(text="Registro guardado", fg_color="green")
            llenar_tabla()
            limpiar()
        else:
            lblMensaje.configure(text="Campos no deben estar vacíos", fg_color="red")

    def actualizar():
        seleccion = tvciudad.selection()
        if seleccion:
            id = seleccion[0]
            val = (nombre.get(), id)
            sql = "UPDATE ciudad SET nombreCiudad=%s WHERE id=%s"
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMensaje.configure(text="Registro actualizado", fg_color="green")
            llenar_tabla()
            limpiar()
        else:
            lblMensaje.configure(text="Seleccione un registro", fg_color="red")
        
    # Crear el marco principal para la pantalla de ciudad
    marco_ciudad = ctk.CTkFrame(frame, fg_color="transparent")
    marco_ciudad.pack(fill="both", expand=True, padx=20, pady=20)

    # Crear los widgets dentro del marco de ciudad
    ctk.CTkLabel(marco_ciudad, text="Nombre Ciudad", text_color=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    txtNombre = ctk.CTkEntry(marco_ciudad, textvariable=nombre, fg_color="white", text_color=COLOR_TEXTO)
    txtNombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(marco_ciudad, text="ID Ciudad", text_color=COLOR_TEXTO).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    txtIdCiudad = ctk.CTkEntry(marco_ciudad, textvariable=filtro_id, fg_color="white", text_color=COLOR_TEXTO)
    txtIdCiudad.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    txtIdCiudad.bind("<KeyRelease>", lambda event: llenar_tabla())

    ctk.CTkLabel(marco_ciudad, text="Nombre Ciudad", text_color=COLOR_TEXTO).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    txtNombreCiudad = ctk.CTkEntry(marco_ciudad, textvariable=filtro_nombre, fg_color="white", text_color=COLOR_TEXTO)
    txtNombreCiudad.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    txtNombreCiudad.bind("<KeyRelease>", lambda event: llenar_tabla())

    lblMensaje = ctk.CTkLabel(marco_ciudad, text="", fg_color="transparent", text_color=COLOR_TEXTO)
    lblMensaje.grid(row=3, column=0, columnspan=2, pady=10)

    # Botones de acciones
    btnNuevo = ctk.CTkButton(marco_ciudad, text="Guardar", command=nuevo, fg_color=COLOR_BOTON)
    btnNuevo.grid(row=4, column=0, pady=10, sticky="ew")

    btnModificar = ctk.CTkButton(marco_ciudad, text="Modificar", command=actualizar, fg_color=COLOR_BOTON)
    btnModificar.grid(row=4, column=1, pady=10, sticky="ew")

    btnEliminar = ctk.CTkButton(marco_ciudad, text="Eliminar", command=eliminar, fg_color=COLOR_BOTON)
    btnEliminar.grid(row=5, column=0, pady=10, sticky="ew")

    btnMostrarTodos = ctk.CTkButton(marco_ciudad, text="Mostrar Todos", command=llenar_tabla, fg_color=COLOR_BOTON)
    btnMostrarTodos.grid(row=5, column=1, pady=10, sticky="ew")

    # Tabla de datos
    tvciudad = ttk.Treeview(marco_ciudad, columns=("ID Ciudad", "Nombre Ciudad"), show="headings")
    tvciudad.heading("ID Ciudad", text="ID Ciudad")
    tvciudad.heading("Nombre Ciudad", text="Nombre Ciudad")
    tvciudad.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    tvciudad.bind("<<TreeviewSelect>>", seleccionar)

    # Botones de paginación
    btnPrev = ctk.CTkButton(marco_ciudad, text="<< Anterior", command=prev_page, fg_color=COLOR_BOTON)
    btnPrev.grid(row=7, column=0, pady=10, sticky="ew")

    btnNext = ctk.CTkButton(marco_ciudad, text="Siguiente >>", command=next_page, fg_color=COLOR_BOTON)
    btnNext.grid(row=7, column=1, pady=10, sticky="ew")

    # Configurar la expansión de la fila del Treeview
    marco_ciudad.grid_rowconfigure(6, weight=1)
    marco_ciudad.grid_columnconfigure(1, weight=1)

    # Llenar la tabla inicialmente
    llenar_tabla()


def mostrar_cargo(frame):
    pass

def mostrar_tipodecontrato(frame):
    pass

def mostrar_dependencia(frame):
    pass

def mostrar_departamento(frame):
    pass

def mostrar_rh(frame):
    pass

def mostrar_genero(frame):
    pass

def mostrar_tipodedocumento(frame):
    pass

def mostrar_tipo_cuenta(frame):
    pass

def mostrar_contrato(frame):
    pass

def mostrar_Contratista(frame):
    pass

def mostrar_jefes(frame):
    pass

def mostrar_usuario(frame):
    pass

def pantalla_bienvenida():
    global usuario_iniciado
    for widget in pantalla.winfo_children():
        widget.destroy()
    
    if not usuario_iniciado:
        messagebox.showinfo(title="Acceso Denegado", message="Inicie sesión primero")
        return

    bienvenida = ctk.CTkToplevel()
    bienvenida.title("Vista de administrador ~ CENIGRAF")
    bienvenida.state("zoomed")  # Se ajusta a un tamaño manejable
    bienvenida.configure(fg_color="#AFFFAF")

    # Cargar fuente Zurich
    fuente_zurich = ctk.CTkFont(family="Zurich.ttf", weight="bold", size=14)

    # Barra superior
    top_frame = ctk.CTkFrame(bienvenida, fg_color="#4CD14C", height=50, corner_radius=0)
    top_frame.pack(side="top", fill="x")

    cerrar_sesion_button = ctk.CTkButton(
        top_frame, text="Cerrar Sesión", command=lambda: cerrar_sesion(bienvenida),
        font=fuente_zurich, fg_color="#FF0022", hover_color="#9E0015",
        corner_radius=10, border_width=2, border_color="#9E0015"
    )
    cerrar_sesion_button.pack(side="right", padx=10, pady=10)

    # Contenedor principal
    main_frame = ctk.CTkFrame(bienvenida, fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    # Menú lateral fijo
    menu_frame = ctk.CTkFrame(
        main_frame, fg_color="#5DFF5D", width=220, corner_radius=15,
        border_width=2, border_color="white"
    )
    menu_frame.pack(side="left", fill="y", padx=10, pady=10)

    # Contenedor de contenido
    contenido_frame = ctk.CTkFrame(main_frame, fg_color="#AFFFAF", corner_radius=15)
    contenido_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Opciones del menú
    pantallas = [
        "Pantalla ARL", "Pantalla EPS", "Pantalla Bancos", "Pantalla Ciudad", "Pantalla Cargo",
        "Pantalla Tipo de contrato", "Pantalla Dependencia", "Pantalla Departamento", "Pantalla RH",
        "Pantalla Género", "Pantalla Tipo de documento", "Pantalla Tipo de Cuenta", "Pantalla Contrato",
        "Pantalla Contratistas", "Pantalla Jefe", "Pantalla Registro Usuarios"
    ]

    for texto in pantallas:
        boton = ctk.CTkButton(
            menu_frame, text=texto, command=lambda t=texto: abrir_pantalla(contenido_frame, t),
            font=fuente_zurich, fg_color="#058A15", hover_color="#035E0E",
            corner_radius=10, border_width=2, border_color="#058A15"
        )
        boton.pack(fill="x", padx=10, pady=5)

######################################################################### Pantalla de inicio ########################################################################################
def mostrar_pantalla_inicial():
    global pantalla, image
    if pantalla is None:
        pantalla = ctk.CTk()
        pantalla.geometry("900x600")
        pantalla.resizable(False,False)
        pantalla.title("Contratistas CENIGRAF")
        pantalla.configure(fg_color="white")

    # Limpiar la pantalla
    for widget in pantalla.winfo_children():
        widget.destroy()
    
    # Intentar cargar el icono de la aplicación
    try:
        pantalla.iconbitmap("logo.ico")
    except:
        print("Advertencia: No se pudo cargar el icono 'logo.ico'")

    # Cargar y ajustar la imagen de fondo
    try:
        image = Image.open("fondo.png")
        image = image.resize((900, 600))  # Ajustar tamaño sin deformar
        image = ctk.CTkImage(image, size=(900, 600))
        fondo_label = ctk.CTkLabel(pantalla, image=image, text="")  # Fondo sin texto
        fondo_label.place(relwidth=1, relheight=1)
    except:
        print("Advertencia: No se pudo cargar la imagen.")

    # Fuente personalizada
    fuente_titulo = ctk.CTkFont(family="Zurich", size=32, weight="bold")
    fuente_botones = ctk.CTkFont(family="Zurich", size=22)

    # Título de acceso
    acceso_label = ctk.CTkLabel(pantalla, text="Acceso al sistema", fg_color="white", text_color=COLOR_BOTON, font=fuente_titulo)
    acceso_label.place(relx=0.5, rely=0.25, anchor="center")

    # Contenedor de botones con padding y diseño limpio
    botones_frame = ctk.CTkFrame(pantalla, fg_color="white", corner_radius=0)
    botones_frame.place(relx=0.5, rely=0.8, anchor="center")

    # Botón "Iniciar Sesión"
    btn_inicio = ctk.CTkButton(
        botones_frame, text="Iniciar Sesión", command=inicio_sesion,
        width=200, height=50, font=fuente_botones,
        fg_color=COLOR_BOTON, hover_color=COLOR_BOTON_HOVER, corner_radius=10
    )
    btn_inicio.pack(pady=15, padx=20)

    # Botón "Restaurar Contraseña"
    btn_restaurar = ctk.CTkButton(
        botones_frame, text="Restaurar Contraseña", command=mostrar_pantalla_restaurar,
        width=200, height=50, font=fuente_botones,
        fg_color=COLOR_BOTON, hover_color=COLOR_BOTON_HOVER, corner_radius=10
    )
    btn_restaurar.pack(pady=15, padx=20)

    pantalla.mainloop()

############################################################################## Validar inicio de sesion ##############################################################################
def validacion_datos(pantalla_sesion):
    global usuario_iniciado
    usuario = usuario_entry.get().strip()
    contrasena = contra_entry.get().strip()

    # Conectar a la base de datos
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="contrataciones"
    )
    fcursor = bd.cursor()

    if not usuario or not contrasena:
        messagebox.showinfo(title="Error", message="Por favor, ingrese ambos campos")
        return

    # Consultar la contraseña en la base de datos
    sql = "SELECT contraseñaCli, idRol FROM usuarios WHERE correoCli=%s"
    fcursor.execute(sql, (usuario,))
    resultado = fcursor.fetchone()

    if resultado:
        hashed_password, rol = resultado  # Extraemos la contraseña y el rol
        if bcrypt.checkpw(contrasena.encode('utf-8'), hashed_password.encode('utf-8')):
            # Dependiendo del rol, abre una ventana diferente
            usuario_iniciado=True
            pantalla_sesion.withdraw()
            if rol == 1:
                pantalla_sesion.destroy()
            elif rol == 2:
                pantalla_bienvenida()
                
            else:
                messagebox.showerror("Error", "Rol desconocido")
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
    else:
        messagebox.showerror("Error", "Usuario no encontrado")
    fcursor.close()
    bd.close()

###################################################################################### Inicio de Sesion ##############################################################################
def inicio_sesion(): 
    global usuario_entry, contra_entry, image
    for widget in pantalla.winfo_children():
        widget.destroy()  # Limpiar la pantalla antes de mostrar la nueva ventana

    # Cargar fondo de pantalla
    try:
        image = Image.open("fondoLogin.png")
        image = image.resize((900, 600))  # Ajustar tamaño sin deformar
        image = ctk.CTkImage(image, size=(900, 600))
        fondo_label = ctk.CTkLabel(pantalla, image=image, text="")
        fondo_label.place(relwidth=1, relheight=1)
    except:
        print("Advertencia: No se pudo cargar la imagen de fondo.")

    fuente_titulos = ctk.CTkFont(family="Zurich.ttf", weight="bold", size=32)
    fuente = ctk.CTkFont(family="Zurich", size=24)
    fuente_botones = ctk.CTkFont(family="Zurich", size=22)

    # Título de acceso
    acceso_label = ctk.CTkLabel(pantalla, text="Iniciar Sesión", fg_color="white", text_color=COLOR_BOTON, font=fuente_titulos)
    acceso_label.place(relx=0.5, rely=0.2, anchor="center")

    # Contenedor principal con bordes redondeados
    container = ctk.CTkFrame(pantalla, fg_color="white", corner_radius=20)
    container.place(relx=0.5, rely=0.55, anchor="center")

    # Campos de entrada
    ctk.CTkLabel(container, text="Correo electrónico", text_color="#446344", font=fuente).pack(anchor="w", pady=5, padx=20)
    usuario_entry = ctk.CTkEntry(container, width=300, font=fuente, fg_color="white", text_color="black", border_width=2)
    usuario_entry.pack(pady=10, padx=20)

    ctk.CTkLabel(container, text="Contraseña", text_color="#446344", font=fuente).pack(anchor="w", pady=5, padx=20)
    contra_entry = ctk.CTkEntry(container, show="*", width=300, font=fuente, fg_color="white", text_color="black", border_width=2)
    contra_entry.pack(pady=10, padx=20)

    # Contenedor de botones con bordes redondeados
    botones_frame = ctk.CTkFrame(container, fg_color="white", corner_radius=10)  
    botones_frame.pack(pady=25)

    ctk.CTkButton(botones_frame, text="Iniciar Sesión", command=lambda: validacion_datos(pantalla),
                  width=120, height=40, font=fuente_botones, fg_color=COLOR_BOTON, hover_color=COLOR_BOTON_HOVER).grid(row=0, column=0, padx=15)

    ctk.CTkButton(botones_frame, text="Regresar", command=mostrar_pantalla_inicial, 
                  width=120, height=40, font=fuente_botones, fg_color=COLOR_BOTON, hover_color=COLOR_BOTON_HOVER).grid(row=0, column=1, padx=15)
################################################################################ Restaurar contraseña ##############################################################################

def validar_datos():
    cedula = entry_cedula.get().strip()
    correo = entry_correo.get().strip()

    if not cedula or not correo:
        messagebox.showerror("Error", "Por favor, complete ambos campos.")
        return

    bd = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="contrataciones"
        )
    fcursor = bd.cursor()
    sql="SELECT id FROM usuarios WHERE numeroCedulaCliente =%s AND correoCli =%s"
    fcursor.execute(sql,(cedula,correo))
    usuario = fcursor.fetchone()
    if usuario:
        mostrar_campo_contraseña(usuario[0])
    else:
        messagebox.showerror("Error", "No se encontró un usuario con los datos ingresados.")
    fcursor.close()
    db.close()

def mostrar_campo_contraseña(user_id):
    global entry_nueva_contraseña, boton_cambiar

    if "entry_nueva_contraseña" in globals():
        return  # Evitar duplicar el campo de contraseña
    
    fuente = ctk.CTkFont(family="Zurich", size=24)
    fuente_botones = ctk.CTkFont(family="Zurich", size=22)

    # Campo de nueva contraseña
    ctk.CTkLabel(container, text="Nueva Contraseña", text_color="#446344", font=fuente).grid(row=3, column=0, sticky="w", pady=5, padx=10)
    entry_nueva_contraseña = ctk.CTkEntry(container, width=300, font=fuente, show="*", fg_color="white", text_color="black")
    entry_nueva_contraseña.grid(row=4, column=0, pady=5, padx=10)

    # Botón para actualizar la contraseña
    boton_cambiar = ctk.CTkButton(container, text="Actualizar Contraseña", command=lambda: actualizar_contraseña(user_id),
                                  width=200, font=fuente_botones, fg_color="green")
    boton_cambiar.grid(row=5, column=0, pady=15)

def actualizar_contraseña(user_id):
    nueva_contraseña = entry_nueva_contraseña.get().strip()

    if not nueva_contraseña:
        messagebox.showerror("Error", "La nueva contraseña no puede estar vacía.")
        return

    # Encriptar la contraseña con bcrypt
    hashed_password = bcrypt.hashpw(nueva_contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        bd = pymysql.connect(host="localhost", user="root", password="", db="contrataciones")
        fcursor = bd.cursor()
        sql = "UPDATE usuarios SET contraseñaCli = %s WHERE id = %s"
        fcursor.execute(sql, (hashed_password, user_id))
        bd.commit()
        messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar la contraseña.\n{str(e)}")
    finally:
        fcursor.close()
        bd.close()

    inicio_sesion()

def mostrar_pantalla_restaurar():
    global pantalla, entry_cedula, entry_correo, container

    for widget in pantalla.winfo_children():
        widget.destroy()  # Limpiar la pantalla antes de cargar la nueva vista

    # Fondo de pantalla
    try:
        image = Image.open("fondoLogin.png")
        image = image.resize((900, 600))  # Ajustar tamaño sin deformar
        image = ctk.CTkImage(image, size=(900, 600))
        fondo_label = ctk.CTkLabel(pantalla, image=image, text="")
        fondo_label.place(relwidth=1, relheight=1)
    except:
        print("Advertencia: No se pudo cargar la imagen de fondo.")

    fuente_titulos = ctk.CTkFont(family="Zurich.ttf", weight="bold", size=32)
    fuente = ctk.CTkFont(family="Zurich", size=24)
    fuente_botones = ctk.CTkFont(family="Zurich", size=22)

    # Título
    acceso_label = ctk.CTkLabel(pantalla, text="Restaurar Contraseña", fg_color="white", text_color=COLOR_BOTON, font=fuente_titulos)
    acceso_label.place(relx=0.5, rely=0.2, anchor="center")

    # Contenedor para los campos
    container = ctk.CTkFrame(pantalla, fg_color="white", corner_radius=20)
    container.place(relx=0.5, rely=0.55, anchor="center")

    # Etiquetas y entradas
    ctk.CTkLabel(container, text="Número de Cédula", text_color="#446344", font=fuente).grid(row=0, column=0, sticky="w", pady=5, padx=10)
    entry_cedula = ctk.CTkEntry(container, width=300, font=fuente, fg_color="white", text_color="black")
    entry_cedula.grid(row=1, column=0, pady=5, padx=10)

    ctk.CTkLabel(container, text="Correo Electrónico", text_color="#446344", font=fuente).grid(row=2, column=0, sticky="w", pady=5, padx=10)
    entry_correo = ctk.CTkEntry(container, width=300, font=fuente, fg_color="white", text_color="black")
    entry_correo.grid(row=3, column=0, pady=5, padx=10)

    # Contenedor para botones
    botones_frame = ctk.CTkFrame(container, fg_color="white")
    botones_frame.grid(row=4, column=0, pady=15)

    ctk.CTkButton(botones_frame, text="Validar", width=120, height=40, font=fuente_botones, fg_color=COLOR_BOTON, command=validar_datos).grid(row=0, column=0, padx=10, pady=15)
    ctk.CTkButton(botones_frame, text="Regresar", command=mostrar_pantalla_inicial, width=120, height=40, font=fuente_botones, fg_color=COLOR_BOTON).grid(row=0, column=1, padx=10, pady=15)
# Función para cerrar sesión
def cerrar_sesion(ventana):
    global usuario_iniciado,pantalla
    usuario_iniciado = False
    ventana.destroy()
    pantalla=None
    inicio_sesion()

# Iniciar la aplicación
mostrar_pantalla_inicial()