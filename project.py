import customtkinter as ctk
from tkinter import messagebox, ttk, filedialog, font
import pymysql
import pandas as pd
import os, bcrypt, re
from PIL import Image
import ctkdlib
import tkinter as tk
import datetime
from tkcalendar import DateEntry
from num2words import num2words 
from dateutil.relativedelta import relativedelta
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx2pdf import convert
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

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
        "Pantalla Tipo de Cuenta": mostrar_tipo_cuenta,
        "Pantalla Contrato": mostrar_contrato,
        "Pantalla Contratistas": mostrar_Contratista,
        "Pantalla Jefe": mostrar_jefes,
        "Pantalla Registro Usuarios": mostrar_usuario
    }
    
    if titulo in funciones_pantalla:
        funciones_pantalla[titulo](contenido_frame)

############################################# Pantalla EPS ######################################################
# Función para mostrar la pantalla de EPS
def mostrar_eps(frame, db):
    modificar = False
    dni = ctk.StringVar()
    nombre = ctk.StringVar()
    eps_id = None  # Variable para almacenar el ID seleccionado

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
        """Cuando se selecciona un registro, actualiza el campo de nombre."""
        nonlocal eps_id
        seleccion = tveps.selection()
        if seleccion:
            eps_id = seleccion[0]  # Guarda el ID seleccionado
            valores = tveps.item(eps_id, "values")
            dni.set(valores[0])
            nombre.set(valores[1])

    def llenar_tabla(filtro=""):
        """Llena la tabla con los registros filtrados en tiempo real."""
        vaciar_tabla()
        sql = "SELECT id, nombreEPS FROM eps WHERE nombreEPS LIKE %s"
        db.cursor.execute(sql, (f"%{filtro}%",))
        filas = db.cursor.fetchall()
        for fila in filas:
            tveps.insert("", 'end', iid=fila[0], text=fila[0], values=(fila[0], fila[1]))

    def actualizar():
        """Actualiza el nombre de la EPS seleccionada."""
        nonlocal eps_id
        if eps_id and nombre.get().strip():
            sql = "UPDATE eps SET nombreEPS=%s WHERE id=%s"
            db.cursor.execute(sql, (nombre.get(), eps_id))
            db.connection.commit()
            llenar_tabla(nombre.get())  # Recargar tabla con el nuevo nombre
        else:
            print("Seleccione un registro válido.")  # Mensaje interno

    def vaciar_tabla():
        """Limpia la tabla antes de llenarla nuevamente."""
        for fila in tveps.get_children():
            tveps.delete(fila)

    # Crear el marco principal
    marco = ctk.CTkFrame(frame, fg_color="transparent")
    marco.pack(fill="both", expand=True, padx=20, pady=20)

    # Campo DNI (No se filtra con este)
    ctk.CTkLabel(marco, text="DNI", text_color=COLOR_TEXTO).grid(column=0, row=0, padx=5, pady=5)
    txtDni = ctk.CTkEntry(marco, textvariable=dni, fg_color="white", text_color=COLOR_TEXTO)
    txtDni.grid(column=1, row=0)

    # Campo Nombre (Se usa para filtrar en tiempo real)
    ctk.CTkLabel(marco, text="Nombre", text_color=COLOR_TEXTO).grid(column=0, row=1, padx=5, pady=5)
    txtNombre = ctk.CTkEntry(marco, textvariable=nombre, fg_color="white", text_color=COLOR_TEXTO)
    txtNombre.grid(column=1, row=1)
    txtNombre.bind("<KeyRelease>", lambda event: llenar_tabla(nombre.get()))  # Filtrar conforme se escribe

    # Tabla de EPS
    tveps = ttk.Treeview(marco, selectmode='browse')
    tveps["columns"] = ("DNI", "Nombre")
    tveps.column("#0", width=0, stretch='no')
    tveps.column("DNI", width=150, anchor='center')
    tveps.column("Nombre", width=150, anchor='center')
    tveps.heading("#0", text="")
    tveps.heading("DNI", text="DNI", anchor='center')
    tveps.heading("Nombre", text="Nombre", anchor='center')
    tveps.grid(column=0, row=2, columnspan=4, padx=5, pady=10, sticky="nsew")
    tveps.bind("<<TreeviewSelect>>", seleccionar)  # Asigna evento de selección

    # Botones
    btnEliminar = ctk.CTkButton(marco, text="Eliminar", command=lambda: eliminar(), fg_color=COLOR_BOTON)
    btnEliminar.grid(column=1, row=3)

    btnNuevo = ctk.CTkButton(marco, text="Guardar", command=lambda: nuevo(), fg_color=COLOR_BOTON)
    btnNuevo.grid(column=2, row=3)

    btnModificar = ctk.CTkButton(marco, text="Modificar", command=actualizar, fg_color=COLOR_BOTON)
    btnModificar.grid(column=3, row=3)

    btnExportar = ctk.CTkButton(marco, text="Exportar a Excel", command=exportar_a_excel_eps, fg_color=COLOR_BOTON)
    btnExportar.grid(column=2, row=4, pady=10)

    btnImportar = ctk.CTkButton(marco, text="Importar de Excel", command=importar_de_excel_eps, fg_color=COLOR_BOTON)
    btnImportar.grid(column=3, row=4, pady=10)

    def eliminar():
        """Elimina el registro seleccionado."""
        seleccion = tveps.selection()
        if seleccion:
            id_real = tveps.item(seleccion[0], "values")[0]
            sql = "DELETE FROM eps WHERE id=%s"
            db.cursor.execute(sql, (id_real,))
            db.connection.commit()
            tveps.delete(seleccion[0])
            limpiar()

    def nuevo():
        """Guarda un nuevo registro."""
        if validar():
            sql = "INSERT INTO eps (id, nombreEPS) VALUES (%s, %s)"
            db.cursor.execute(sql, (dni.get(), nombre.get()))
            db.connection.commit()
            llenar_tabla()
            limpiar()
        else:
            print("Los campos no deben estar vacíos.")  # Mensaje interno

    def validar():
        """Valida que los campos no estén vacíos."""
        return len(dni.get().strip()) > 0 and len(nombre.get().strip()) > 0

    def limpiar():
        """Limpia los campos de entrada."""
        dni.set("")
        nombre.set("")

    # Llenar la tabla al iniciar
    llenar_tabla("")

######################################### Pantalla ARL #########################################################
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

####################################### Pantalla de banco #####################################################
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

############################################# Pantalla Ciudad ####################################################
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
    ctk.CTkLabel(marco_ciudad, text="Agregar Ciudad", text_color=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    txtNombre = ctk.CTkEntry(marco_ciudad, textvariable=nombre, fg_color="white", text_color=COLOR_TEXTO)
    txtNombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(marco_ciudad, text="Buscar Ciudad", text_color=COLOR_TEXTO).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    txtNombreCiudad = ctk.CTkEntry(marco_ciudad, textvariable=filtro_nombre, fg_color="white", text_color=COLOR_TEXTO)
    txtNombreCiudad.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    txtNombreCiudad.bind("<KeyRelease>", lambda event: llenar_tabla())

    lblMensaje = ctk.CTkLabel(marco_ciudad, text="", fg_color="transparent", text_color=COLOR_TEXTO)
    lblMensaje.grid(row=3, column=0, columnspan=2, pady=10)

    # Botones de acciones
    btnNuevo = ctk.CTkButton(marco_ciudad, text="Nuevo", command=nuevo, fg_color=COLOR_BOTON)
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

########################################### Pantalla Cargo #####################################################
def mostrar_cargo(frame):
    global db, records_per_page, page_number, total_records
    
    db = DataBase()
    records_per_page = 10
    page_number = 1
    total_records = 0
    
    # Variables de control
    id_cargo = ctk.StringVar()
    nombre_cargo = ctk.StringVar()
    id_jefe = ctk.StringVar()
    filtro_nombre_cargo = ctk.StringVar()
    filtro_jefe = ctk.StringVar()
    
    def cargar_nombres_cargo():
        db.cursor.execute("SELECT DISTINCT nombreCargo FROM cargo")
        return [fila[0] for fila in db.cursor.fetchall()]
    
    def cargar_jefes():
        db.cursor.execute("SELECT id, nombreJefe FROM jefe")
        return db.cursor.fetchall()
    
    def obtener_nombre_jefe(id_jefe):
        db.cursor.execute("SELECT nombreJefe FROM jefe WHERE id=%s", (id_jefe,))
        result = db.cursor.fetchone()
        return result[0] if result else "Desconocido"

    def obtener_id_jefe(nombre_jefe):
        db.cursor.execute("SELECT id FROM jefe WHERE nombreJefe=%s", (nombre_jefe,))
        result = db.cursor.fetchone()
        return result[0] if result else None
    
    def seleccionar(event):
        seleccion = tvCargos.selection()
        if seleccion:
            id = seleccion[0]
            valores = tvCargos.item(id, "values")
            id_cargo.set(valores[0])
            nombre_cargo.set(valores[1])
            id_jefe.set(obtener_id_jefe(valores[2]))
    
    def limpiar():
        id_cargo.set("")
        nombre_cargo.set("")
        id_jefe.set("")
        comboJefe.set("")

    def vaciar_tabla():
        for fila in tvCargos.get_children():
            tvCargos.delete(fila)
    
    def llenar_tabla():
        vaciar_tabla()
        offset = (page_number - 1) * records_per_page
        
        sql = """
        SELECT c.id, c.nombreCargo, j.nombreJefe
        FROM cargo c
        JOIN jefe j ON c.idJefe = j.id
        WHERE 1=1
        """
        valores = []

        if filtro_nombre_cargo.get():
            sql += " AND c.nombreCargo = %s"
            valores.append(filtro_nombre_cargo.get())
        if filtro_jefe.get():
            sql += " AND j.nombreJefe = %s"
            valores.append(filtro_jefe.get())
        
        sql += " LIMIT %s OFFSET %s"
        valores.extend([records_per_page, offset])
        
        db.cursor.execute(sql, tuple(valores))
        for fila in db.cursor.fetchall():
            tvCargos.insert("", 'end', fila[0], text=fila[0], values=(fila[0], fila[1], fila[2]))
    
    def validar():
        return len(nombre_cargo.get()) > 0

    def nuevo():
        if validar():
            sql = "INSERT INTO cargo (id, nombreCargo, idJefe) VALUES (%s, %s, %s)"
            db.cursor.execute(sql, (id_cargo.get(), nombre_cargo.get(), id_jefe.get()))
            db.connection.commit()
            llenar_tabla()
            limpiar()
    
    def actualizar():
        seleccion = tvCargos.selection()
        if seleccion:
            id = seleccion[0]
            sql = "UPDATE cargo SET nombreCargo=%s, idJefe=%s WHERE id=%s"
            db.cursor.execute(sql, (nombre_cargo.get(), id_jefe.get(), id))
            db.connection.commit()
            llenar_tabla()
            limpiar()
    
    def eliminar():
        seleccion = tvCargos.selection()
        if seleccion:
            id = seleccion[0]
            db.cursor.execute("DELETE FROM cargo WHERE id=%s", (id,))
            db.connection.commit()
            tvCargos.delete(id)
            limpiar()
    
    # Crear el marco principal para la pantalla de cargos
    marco_cargo = ctk.CTkFrame(frame, fg_color="transparent")
    marco_cargo.pack(fill="both", expand=True, padx=20, pady=20)

    # Crear los widgets dentro del marco de cargo
    ctk.CTkLabel(marco_cargo, text="ID Cargo", text_color=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    txtIdCargo = ctk.CTkEntry(marco_cargo, textvariable=id_cargo, fg_color="white", text_color=COLOR_TEXTO)
    txtIdCargo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(marco_cargo, text="Nombre Cargo", text_color=COLOR_TEXTO).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    txtNombreCargo = ctk.CTkEntry(marco_cargo, textvariable=nombre_cargo, fg_color="white", text_color=COLOR_TEXTO)
    txtNombreCargo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(marco_cargo, text="Jefe", text_color=COLOR_TEXTO).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    jefes = cargar_jefes()
    jefes_dict = {jefe[1]: jefe[0] for jefe in jefes}
    comboJefe = ttk.Combobox(marco_cargo, values=list(jefes_dict.keys()), textvariable=obtener_nombre_jefe)
    comboJefe.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    comboJefe.bind("<<ComboboxSelected>>", lambda e: id_jefe.set(jefes_dict.get(comboJefe.get(), "")))

    lblMensaje = ctk.CTkLabel(marco_cargo, text="", fg_color="transparent", text_color=COLOR_TEXTO)
    lblMensaje.grid(row=3, column=0, columnspan=2, pady=10)

    # Botones de acciones
    btnNuevo = ctk.CTkButton(marco_cargo, text="Guardar", command=nuevo, fg_color=COLOR_BOTON)
    btnNuevo.grid(row=4, column=0, pady=10, sticky="ew")

    btnModificar = ctk.CTkButton(marco_cargo, text="Modificar", command=actualizar, fg_color=COLOR_BOTON)
    btnModificar.grid(row=4, column=1, pady=10, sticky="ew")

    btnEliminar = ctk.CTkButton(marco_cargo, text="Eliminar", command=eliminar, fg_color=COLOR_BOTON)
    btnEliminar.grid(row=5, column=0, pady=10, sticky="ew")

    btnMostrarTodos = ctk.CTkButton(marco_cargo, text="Mostrar Todos", command=llenar_tabla, fg_color=COLOR_BOTON)
    btnMostrarTodos.grid(row=5, column=1, pady=10, sticky="ew")

    # Tabla de datos
    tvCargos = ttk.Treeview(marco_cargo, columns=("ID", "Nombre Cargo", "Jefe"), show="headings")
    tvCargos.heading("ID", text="ID")
    tvCargos.heading("Nombre Cargo", text="Nombre Cargo")
    tvCargos.heading("Jefe", text="Jefe")
    tvCargos.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    tvCargos.bind("<<TreeviewSelect>>", seleccionar)

    # Configurar la expansión de la fila del Treeview
    marco_cargo.grid_rowconfigure(6, weight=1)
    marco_cargo.grid_columnconfigure(1, weight=1)

    # Llenar la tabla inicialmente
    llenar_tabla()

##################################### Tipo de contrato ##################################################################
def mostrar_tipodecontrato(frame):
    global db, page_number, records_per_page, total_records
    db = DataBase()
    modificar = False
    id_tipo = ctk.StringVar()
    nombre_tipo = ctk.StringVar()
    filtro_nombre_tipo = ctk.StringVar()  # Variable para el filtro del combobox

    # Variables de paginación
    page_number = 1
    records_per_page = 10
    total_records = 0

    # Función para exportar a Excel
    def exportar_a_excel_tipodecontrato():
        try:
            sql = "SELECT id, nombreTipoContrato FROM tipodecontrato"
            db.cursor.execute(sql)
            datos = db.cursor.fetchall()

            df = pd.DataFrame(datos, columns=["ID Tipo", "Nombre Tipo"])
            nombre_archivo = "tipos_de_contrato.xlsx"
            df.to_excel(nombre_archivo, index=False)

            lblMensaje.configure(text=f"Datos exportados a {nombre_archivo}", fg_color="green")
        except Exception as e:
            lblMensaje.configure(text=f"Error al exportar: {str(e)}", fg_color="red")

    # Función para importar desde Excel
    def importar_desde_excel_tipodecontrato():
        try:
            archivo_excel = filedialog.askopenfilename(
                title="Seleccionar archivo de Excel",
                filetypes=[("Archivos de Excel", ".xlsx"), ("Todos los archivos", ".*")]
            )

            if archivo_excel:
                df = pd.read_excel(archivo_excel)

                if "ID Tipo" in df.columns and "Nombre Tipo" in df.columns:
                    for _, fila in df.iterrows():
                        id_tipo = fila["ID Tipo"]
                        nombre_tipo = fila["Nombre Tipo"]

                        sql_verificar = "SELECT id FROM tipodecontrato WHERE id = %s"
                        db.cursor.execute(sql_verificar, (id_tipo,))
                        if db.cursor.fetchone():
                            sql_actualizar = "UPDATE tipodecontrato SET nombreTipoContrato = %s WHERE id = %s"
                            db.cursor.execute(sql_actualizar, (nombre_tipo, id_tipo))
                        else:
                            sql_insertar = "INSERT INTO tipodecontrato (id, nombreTipoContrato) VALUES (%s, %s)"
                            db.cursor.execute(sql_insertar, (id_tipo, nombre_tipo))

                    db.connection.commit()
                    llenar_tabla()
                    lblMensaje.configure(text="Datos importados correctamente", fg_color="green")
                else:
                    lblMensaje.configure(text="El archivo no tiene las columnas correctas", fg_color="red")
        except Exception as e:
            lblMensaje.configure(text=f"Error al importar: {str(e)}", fg_color="red")

    # Función para seleccionar un registro en la tabla
    def seleccionar(event):
        seleccion = tvEstudiantes.selection()
        if seleccion:
            id = seleccion[0]
            valores = tvEstudiantes.item(id, "values")
            id_tipo.set(valores[0])
            nombre_tipo.set(valores[1])
            modificarTrue()

        # Crear el marco principal
    marco = ctk.CTkFrame(frame, fg_color="transparent")
    marco.pack(fill="both", expand=True, padx=20, pady=20)

    # Campos del formulario
    ctk.CTkLabel(marco, text="ID Tipo", text_color=COLOR_TEXTO).grid(column=0, row=0, padx=5, pady=5, sticky="w")
    txtIdTipo = ctk.CTkEntry(marco, textvariable=id_tipo, fg_color="white", text_color=COLOR_TEXTO)
    txtIdTipo.grid(column=1, row=0, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(marco, text="Nombre Tipo", text_color=COLOR_TEXTO).grid(column=0, row=1, padx=5, pady=5, sticky="w")
    txtNombreTipo = ctk.CTkEntry(marco, textvariable=nombre_tipo, fg_color="white", text_color=COLOR_TEXTO)
    txtNombreTipo.grid(column=1, row=1, padx=5, pady=5, sticky="ew")

    # Mensajes de estado
    lblMensaje = ctk.CTkLabel(marco, text="Aquí van los mensajes", fg_color="transparent", text_color=COLOR_TEXTO)
    lblMensaje.grid(column=0, row=2, columnspan=4, pady=10)

    # Configuración del Treeview
    tvEstudiantes = ttk.Treeview(marco, selectmode='none', columns=("ID Tipo", "Nombre Tipo"), show="headings")
    tvEstudiantes.column("ID Tipo", width=150, anchor="center")
    tvEstudiantes.column("Nombre Tipo", width=300, anchor="center")
    tvEstudiantes.heading("ID Tipo", text="ID Tipo", anchor="center")
    tvEstudiantes.heading("Nombre Tipo", text="Nombre Tipo", anchor="center")
    tvEstudiantes.grid(column=0, row=3, columnspan=4, padx=5, pady=10, sticky="nsew")
    tvEstudiantes.bind("<<TreeviewSelect>>", seleccionar)

    # Ajustar la expansión de la tabla
    marco.grid_rowconfigure(3, weight=1)
    marco.grid_columnconfigure(1, weight=1)

    # Combobox para filtrar por nombre
    ctk.CTkLabel(marco, text="Filtrar por Nombre Tipo", text_color=COLOR_TEXTO).grid(column=0, row=4, padx=5, pady=5, sticky="w")
    comboFiltroNombreTipo = ttk.Combobox(marco, textvariable=filtro_nombre_tipo)
    comboFiltroNombreTipo.grid(column=1, row=4, padx=5, pady=5, sticky="ew")

    # Cargar tipos de contrato en el combobox
    def cargar_tipos():
        sql = "SELECT nombreTipoContrato FROM tipodecontrato"
        db.cursor.execute(sql)
        tipos = [fila[0] for fila in db.cursor.fetchall()]
        comboFiltroNombreTipo["values"] = tipos

    cargar_tipos()

    # Función para limpiar campos
    def limpiar_campos():
        id_tipo.set("")
        nombre_tipo.set("")
        filtro_nombre_tipo.set("")

    # Función para aplicar filtro
    def aplicar_filtro(event=None):
        llenar_tabla(filtro=filtro_nombre_tipo.get())
        limpiar_campos()

    # Vincular evento de selección del combobox
    comboFiltroNombreTipo.bind("<<ComboboxSelected>>", aplicar_filtro)

    # Botones de acción
    btnEliminarFiltro = ctk.CTkButton(marco, text="Mostrar Consultas", command=lambda: llenar_tabla(filtro=""), fg_color=COLOR_BOTON)
    btnEliminarFiltro.grid(column=3, row=4, padx=5, pady=5, sticky="ew")

    btnEliminar = ctk.CTkButton(marco, text="Eliminar", command=eliminar, fg_color=COLOR_BOTON)
    btnEliminar.grid(column=1, row=5, padx=5, pady=10, sticky="ew")

    btnNuevo = ctk.CTkButton(marco, text="Guardar", command=nuevo, fg_color=COLOR_BOTON)
    btnNuevo.grid(column=2, row=5, padx=5, pady=10, sticky="ew")

    btnModificar = ctk.CTkButton(marco, text="Seleccionar", command=actualizar, fg_color=COLOR_BOTON)
    btnModificar.grid(column=3, row=5, padx=5, pady=10, sticky="ew")

    # Botones de exportar e importar
    btnExportar = ctk.CTkButton(marco, text="Exportar a Excel", command=exportar_a_excel_tipodecontrato, fg_color=COLOR_BOTON)
    btnExportar.grid(column=2, row=6, padx=5, pady=10, sticky="ew")

    btnImportar = ctk.CTkButton(marco, text="Importar desde Excel", command=importar_desde_excel_tipodecontrato, fg_color=COLOR_BOTON)
    btnImportar.grid(column=3, row=6, padx=5, pady=10, sticky="ew")

    # Paginación
    btnPrev = ctk.CTkButton(marco, text="<< Anterior", command=lambda: cambiar_pagina(-1), fg_color=COLOR_BOTON)
    btnPrev.grid(column=0, row=7, padx=5, pady=10, sticky="ew")

    btnNext = ctk.CTkButton(marco, text="Siguiente >>", command=lambda: cambiar_pagina(1), fg_color=COLOR_BOTON)
    btnNext.grid(column=3, row=7, padx=5, pady=10, sticky="ew")


    # Función para cambiar de página
    def cambiar_pagina(direccion):
        global page_number
        page_number += direccion
        llenar_tabla(filtro=filtro_nombre_tipo.get())

    # Función para actualizar botones de paginación
    def actualizar_botones_paginacion():
        global total_records
        btnPrev.configure(state='normal' if page_number > 1 else 'disabled')
        btnNext.configure(state='normal' if page_number * records_per_page < total_records else 'disabled')

    # Función para llenar la tabla
    def llenar_tabla(filtro=""):
        vaciar_tabla()
        global total_records

        offset = (page_number - 1) * records_per_page

        if filtro:
            sql_count = "SELECT COUNT(*) FROM tipodecontrato WHERE nombreTipoContrato LIKE %s"
            db.cursor.execute(sql_count, ('%' + filtro + '%',))
            total_records = db.cursor.fetchone()[0]

            sql = f"SELECT id, nombreTipoContrato FROM tipodecontrato WHERE nombreTipoContrato LIKE %s LIMIT {records_per_page} OFFSET {offset}"
            db.cursor.execute(sql, ('%' + filtro + '%',))
        else:
            sql_count = "SELECT COUNT(*) FROM tipodecontrato"
            db.cursor.execute(sql_count)
            total_records = db.cursor.fetchone()[0]

            sql = f"SELECT id, nombreTipoContrato FROM tipodecontrato LIMIT {records_per_page} OFFSET {offset}"
            db.cursor.execute(sql)

        filas = db.cursor.fetchall()

        for fila in filas:
            id = fila[0]
            tvEstudiantes.insert("", 'end', id, text=id, values=(fila[0], fila[1]))

        actualizar_botones_paginacion()

    # Función para vaciar la tabla
    def vaciar_tabla():
        filas = tvEstudiantes.get_children()
        for fila in filas:
            tvEstudiantes.delete(fila)

    # Función para validar campos
    def validar():
        return len(id_tipo.get()) > 0 and len(nombre_tipo.get()) > 0

    # Función para limpiar campos
    def limpiar():
        id_tipo.set("")
        nombre_tipo.set("")

    # Función para guardar un nuevo registro
    def nuevo():
        if not modificar:
            if validar():
                val = (id_tipo.get(), nombre_tipo.get())
                sql = "INSERT INTO tipodecontrato (id, nombreTipoContrato) VALUES (%s, %s)"
                db.cursor.execute(sql, val)
                db.connection.commit()
                lblMensaje.configure(text="Se ha guardado el registro con éxito", fg_color="green")
                llenar_tabla()
                limpiar()
            else:
                lblMensaje.configure(text="Los campos no deben estar vacíos", fg_color="red")
        else:
            modificarFalse()

    # Función para eliminar un registro
    def eliminar():
        seleccion = tvEstudiantes.selection()
        if seleccion:
            id = seleccion[0]
            if int(id) > 0:
                sql = "DELETE FROM tipodecontrato WHERE id=%s"
                db.cursor.execute(sql, (id,))
                db.connection.commit()
                tvEstudiantes.delete(id)
                lblMensaje.configure(text="Se ha eliminado el registro correctamente")
                limpiar()
                llenar_tabla()

    # Función para actualizar un registro
    def actualizar():
        if modificar:
            if validar():
                val = (nombre_tipo.get(), id_tipo.get())
                sql = "UPDATE tipodecontrato SET nombreTipoContrato=%s WHERE id=%s"
                db.cursor.execute(sql, val)
                db.connection.commit()
                lblMensaje.configure(text="Se ha modificado el registro con éxito", fg_color="green")
                llenar_tabla()
                limpiar()
            else:
                lblMensaje.configure(text="Los campos no deben estar vacíos", fg_color="red")
        else:
            modificarTrue()

    # Función para habilitar la edición
    def modificarTrue():
        nonlocal modificar
        modificar = True
        tvEstudiantes.config(selectmode='browse')
        btnNuevo.configure(text="Nuevo")
        btnModificar.configure(text="Modificar")
        btnEliminar.configure(state='normal')

    # Función para deshabilitar la edición
    def modificarFalse():
        nonlocal modificar
        modificar = False
        tvEstudiantes.config(selectmode='none')
        btnNuevo.configure(text="Guardar")
        btnModificar.configure(text="Seleccionar")
        btnEliminar.configure(state='disabled')

    # Llenar la tabla al iniciar
    llenar_tabla()

########################################### Pantalla dependencias ########################################################3
def mostrar_dependencia(frame):
    global db
    db = DataBase()
    modificar = False
    id_dependencia = ctk.StringVar()
    nombre_dependencia = ctk.StringVar()
    filtro_nombre = ctk.StringVar()  # Variable para el filtro de Nombre

    # Variables de paginación
    page_number = 1
    records_per_page = 10

    def seleccionar(event):
        seleccion = tvDependencias.selection()
        if seleccion:
            id = seleccion[0]
            valores = tvDependencias.item(id, "values")
            id_dependencia.set(valores[0])
            nombre_dependencia.set(valores[1])

    def vaciar_tabla():
        filas = tvDependencias.get_children()
        for fila in filas:
            tvDependencias.delete(fila)

    def limpiar():
        id_dependencia.set("")
        nombre_dependencia.set("")
        filtro_nombre.set("")  # Limpiar el filtro también

    def llenar_tabla(filtro=None):
        vaciar_tabla()
        try:
            offset = (page_number - 1) * records_per_page
            if filtro:
                sql = "SELECT id, nombreDependencia FROM dependencia WHERE nombreDependencia LIKE %s LIMIT %s OFFSET %s"
                db.cursor.execute(sql, (f"%{filtro}%", records_per_page, offset))
            else:
                sql = "SELECT id, nombreDependencia FROM dependencia LIMIT %s OFFSET %s"
                db.cursor.execute(sql, (records_per_page, offset))
            filas = db.cursor.fetchall()
            for fila in filas:
                id = fila[0]
                tvDependencias.insert("", 'end', id, text=id, values=(fila[0], fila[1]))
        except Exception as e:
            lblMensaje.configure(text=f"Error al llenar la tabla: {e}", fg_color="red")

    def cargar_dependencias_en_combobox():
        try:
            sql = "SELECT DISTINCT nombreDependencia FROM dependencia"
            db.cursor.execute(sql)
            dependencias = db.cursor.fetchall()
            nombres = [fila[0] for fila in dependencias]  # Obtener los nombres de las dependencias
            cbFiltroNombre.configure(values=nombres)  # Actualizar el Combobox con los nombres
        except Exception as e:
            lblMensaje.configure(text=f"Error al cargar nombres: {e}", fg_color="red")

    def modificarFalse():
        nonlocal modificar
        modificar = False
        tvDependencias.config(selectmode='none')
        btnNuevo.configure(text="Guardar")
        btnModificar.configure(text="Seleccionar")
        btnEliminar.configure(state='disabled')

    def modificarTrue():
        nonlocal modificar
        modificar = True
        tvDependencias.config(selectmode='browse')
        btnNuevo.configure(text="Nuevo")
        btnModificar.configure(text="Modificar")
        btnEliminar.configure(state='normal')

    def validar():
        return len(id_dependencia.get()) > 0 and len(nombre_dependencia.get()) > 0

    def eliminar():
        seleccion = tvDependencias.selection()
        if seleccion:
            id = seleccion[0]
            if int(id) > 0:
                sql = "DELETE FROM dependencia WHERE id=%s"
                db.cursor.execute(sql, (id,))
                db.connection.commit()
                tvDependencias.delete(id)
                lblMensaje.configure(text="Se ha eliminado el registro correctamente", fg_color="green")
                limpiar()
                llenar_tabla()
            else:
                lblMensaje.configure(text="Seleccione un registro para eliminar", fg_color="red")

    def nuevo():
        if not modificar:
            if validar():
                val = (id_dependencia.get(), nombre_dependencia.get())
                sql = "INSERT INTO dependencia (id, nombreDependencia) VALUES (%s, %s)"
                try:
                    db.cursor.execute(sql, val)
                    db.connection.commit()
                    lblMensaje.configure(text="Se ha guardado el registro con éxito", fg_color="green")
                    llenar_tabla()
                    limpiar()
                    cargar_dependencias_en_combobox()  # Actualizar el Combobox después de agregar una nueva dependencia
                except pymysql.err.IntegrityError as e:
                    lblMensaje.configure(text=f"Error: {e}", fg_color="red")
            else:
                lblMensaje.configure(text="Los campos no deben estar vacíos", fg_color="red")
        else:
            modificarFalse()

    def actualizar():
        if modificar:
            if validar():
                seleccion = tvDependencias.selection()
                if seleccion:
                    id = seleccion[0]
                    val = (nombre_dependencia.get(),)
                    sql = "UPDATE dependencia SET nombreDependencia=%s WHERE id=%s"
                    try:
                        db.cursor.execute(sql, val + (id,))
                        db.connection.commit()
                        lblMensaje.configure(text="Se ha guardado el registro con éxito", fg_color="green")
                        llenar_tabla()
                        limpiar()
                        cargar_dependencias_en_combobox()  # Actualizar el Combobox después de la actualización
                    except pymysql.err.IntegrityError as e:
                        lblMensaje.configure(text=f"Error: {e}", fg_color="red")
            else:
                lblMensaje.configure(text="Los campos no deben estar vacíos", fg_color="red")
        else:
            modificarTrue()

    def ir_a_pagina_anterior():
        nonlocal page_number
        if page_number > 1:
            page_number -= 1
            llenar_tabla()
            actualizar_botones_paginacion()

    def ir_a_pagina_siguiente():
        nonlocal page_number
        page_number += 1
        llenar_tabla()
        actualizar_botones_paginacion()

    def actualizar_botones_paginacion():
        btnAnterior.configure(state='normal' if page_number > 1 else 'disabled')
        btnSiguiente.configure(state='normal')  

    def aplicar_filtro(event=None):
        filtro = filtro_nombre.get()
        if filtro:
            llenar_tabla(filtro)
        else:
            llenar_tabla()
        limpiar()

    def exportar_a_excel_dependencias():
        try:
            sql = "SELECT id, nombreDependencia FROM dependencia"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            
            if filas:
                df = pd.DataFrame(filas, columns=['ID', 'Nombre'])
                filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                        filetypes=[("Excel files", "*.xlsx"),
                                                                   ("All files", ".")])
                if filepath:
                    df.to_excel(filepath, index=False)
                    messagebox.showinfo("Exportación Exitosa", f"Datos exportados a {filepath}")
                    if os.name == 'nt':  # Solo para Windows
                        os.startfile(filepath)
            else:
                messagebox.showwarning("Sin Datos", "No hay datos para exportar")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar los datos: {e}")

    # Configuración del marco y los widgets
    marco = ctk.CTkFrame(frame, fg_color="transparent")
    marco.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(marco, text="ID", text_color=COLOR_TEXTO).grid(column=0, row=0, padx=5, pady=5)
    txtIdDependencia = ctk.CTkEntry(marco, textvariable=id_dependencia, fg_color="white",text_color=COLOR_TEXTO)
    txtIdDependencia.grid(column=1, row=0)

    ctk.CTkLabel(marco, text="Nombre", text_color=COLOR_TEXTO).grid(column=0, row=1, padx=5, pady=5)
    txtNombreDependencia = ctk.CTkEntry(marco, textvariable=nombre_dependencia, fg_color="white",text_color=COLOR_TEXTO)
    txtNombreDependencia.grid(column=1, row=1)

    # Combobox para filtro por Nombre
    ctk.CTkLabel(marco, text="Filtrar por Nombre", text_color=COLOR_TEXTO).grid(column=0, row=2, padx=5, pady=5)
    cbFiltroNombre = ctk.CTkComboBox(marco,fg_color="white",text_color=COLOR_TEXTO)  # Eliminado textvariable
    cbFiltroNombre.grid(column=1, row=2)
    cbFiltroNombre.bind("<<ComboboxSelected>>", lambda e: filtro_nombre.set(cbFiltroNombre.get()))  # Actualizar la variable

    lblMensaje = ctk.CTkLabel(marco, text="Aquí van los mensajes", fg_color="green")
    lblMensaje.grid(column=0, row=3, columnspan=4)

    tvDependencias = ttk.Treeview(marco, selectmode='none')
    tvDependencias["columns"] = ("ID", "Nombre")
    tvDependencias.column("#0", width=0, stretch='no')
    tvDependencias.column("ID", width=150, anchor='center')
    tvDependencias.column("Nombre", width=150, anchor='center')
    tvDependencias.heading("#0", text="")
    tvDependencias.heading("ID", text="ID", anchor='center')
    tvDependencias.heading("Nombre", text="Nombre", anchor='center')
    tvDependencias.grid(column=0, row=4, columnspan=4, padx=5)
    tvDependencias.bind("<<TreeviewSelect>>", seleccionar)

    btnEliminar = ctk.CTkButton(marco, text="Eliminar", command=eliminar, fg_color=COLOR_BOTON)
    btnEliminar.grid(column=1, row=5)

    btnNuevo = ctk.CTkButton(marco, text="Guardar", command=nuevo, fg_color=COLOR_BOTON)
    btnNuevo.grid(column=2, row=5)

    btnModificar = ctk.CTkButton(marco, text="Seleccionar", command=actualizar, fg_color=COLOR_BOTON)
    btnModificar.grid(column=3, row=5)

    # Botones de Paginación
    btnAnterior = ctk.CTkButton(marco, text="<< Anterior", command=ir_a_pagina_anterior, fg_color=COLOR_BOTON)
    btnAnterior.grid(column=0, row=6)

    btnSiguiente = ctk.CTkButton(marco, text="Siguiente >>", command=ir_a_pagina_siguiente, fg_color=COLOR_BOTON)
    btnSiguiente.grid(column=1, row=6)

    # Botón para exportar a Excel
    btnExportar = ctk.CTkButton(marco, text="Exportar a Excel", command=exportar_a_excel_dependencias, fg_color=COLOR_BOTON)
    btnExportar.grid(column=2, row=6, pady=10)

    llenar_tabla()
    cargar_dependencias_en_combobox()  # Llenar el Combobox con los nombres de las dependencias al iniciar
    actualizar_botones_paginacion()

def mostrar_departamento(frame):
    # Inicializar variables
    db = DataBase()
    modificar = False
    id_departamento = ctk.StringVar()
    nombre_departamento = ctk.StringVar()

    def seleccionar(event):
        seleccion = tvDepartamentos.selection()
        if seleccion:
            id = seleccion[0]
            valores = tvDepartamentos.item(id, "values")
            id_departamento.set(valores[0])
            nombre_departamento.set(valores[1])

    def limpiar():
        id_departamento.set("")
        nombre_departamento.set("")

    def llenar_tabla():
        tvDepartamentos.delete(*tvDepartamentos.get_children())
        sql = "SELECT id, nombreDepartamento FROM departamentos"
        db.cursor.execute(sql)
        for fila in db.cursor.fetchall():
            tvDepartamentos.insert("", 'end', iid=fila[0], values=(fila[0], fila[1]))

    def eliminar():
        seleccion = tvDepartamentos.selection()
        if seleccion:
            id = seleccion[0]
            sql = "DELETE FROM departamentos WHERE id=%s"
            db.cursor.execute(sql, (id,))
            db.connection.commit()
            tvDepartamentos.delete(id)
            lblMensaje.configure(text="Registro eliminado correctamente", text_color="red")
            limpiar()

    def nuevo():
        if id_departamento.get() and nombre_departamento.get():
            sql = "INSERT INTO departamentos (id, nombreDepartamento) VALUES (%s, %s)"
            db.cursor.execute(sql, (id_departamento.get(), nombre_departamento.get()))
            db.connection.commit()
            lblMensaje.configure(text="Registro guardado con éxito", text_color="green")
            llenar_tabla()
            limpiar()

    def actualizar():
        seleccion = tvDepartamentos.selection()
        if seleccion and nombre_departamento.get():
            id = seleccion[0]
            sql = "UPDATE departamentos SET nombreDepartamento=%s WHERE id=%s"
            db.cursor.execute(sql, (nombre_departamento.get(), id))
            db.connection.commit()
            lblMensaje.configure(text="Registro actualizado con éxito", text_color="blue")
            llenar_tabla()
            limpiar()

    # UI con diseño mejorado
    marco = ctk.CTkFrame(frame, fg_color="transparent")
    marco.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(marco, text="Agregar Departamento", text_color=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    txtIdDepartamento = ctk.CTkEntry(marco, textvariable=id_departamento, fg_color="white", text_color=COLOR_TEXTO)
    txtIdDepartamento.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ctk.CTkLabel(marco, text="Nombre Departamento", text_color=COLOR_TEXTO).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    txtNombreDepartamento = ctk.CTkEntry(marco, textvariable=nombre_departamento, fg_color="white", text_color=COLOR_TEXTO)
    txtNombreDepartamento.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    lblMensaje = ctk.CTkLabel(marco, text="", fg_color="transparent", text_color=COLOR_TEXTO)
    lblMensaje.grid(row=2, column=0, columnspan=2, pady=10)

    # Botones de acción
    btnNuevo = ctk.CTkButton(marco, text="Guardar", command=nuevo, fg_color=COLOR_BOTON)
    btnNuevo.grid(row=3, column=0, pady=10, sticky="ew")

    btnModificar = ctk.CTkButton(marco, text="Modificar", command=actualizar, fg_color=COLOR_BOTON)
    btnModificar.grid(row=3, column=1, pady=10, sticky="ew")

    btnEliminar = ctk.CTkButton(marco, text="Eliminar", command=eliminar, fg_color=COLOR_BOTON)
    btnEliminar.grid(row=4, column=0, pady=10, sticky="ew")

    btnMostrarTodos = ctk.CTkButton(marco, text="Mostrar Todos", command=llenar_tabla, fg_color=COLOR_BOTON)
    btnMostrarTodos.grid(row=4, column=1, pady=10, sticky="ew")

    # Tabla de datos
    tvDepartamentos = ttk.Treeview(marco, columns=("ID", "Nombre"), show="headings")
    tvDepartamentos.heading("ID", text="ID Departamento")
    tvDepartamentos.heading("Nombre", text="Nombre Departamento")
    tvDepartamentos.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    tvDepartamentos.bind("<<TreeviewSelect>>", seleccionar)

    # Ajuste de expansión
    marco.grid_rowconfigure(5, weight=1)
    marco.grid_columnconfigure(1, weight=1)

    llenar_tabla()

def mostrar_tipo_cuenta(frame):
    pass


    
    
def formatear_fecha_larga(fecha):
    return fecha.strftime("%d de %B de %Y")  # Formato: 22 de enero de 2024

def mostrar_contrato(frame):
    db = DataBase()
    modificar = False
    descripcion_contrato = tk.StringVar()
    autorizacion_contratos = tk.StringVar()
    valor_contrato = tk.StringVar()
    obligaciones_especificas = tk.StringVar()
    consecutivo = tk.StringVar()
    id_independiente = tk.StringVar()
    id_version = tk.StringVar()
    id_objeto = tk.StringVar()

    # Variables de paginación
    page_number = 1
    records_per_page = 10

    # Variables de filtro
    filtro_cliente = tk.StringVar()
    filtro_tipo_contrato = tk.StringVar()
    filtro_cargo = tk.StringVar()
    filtro_dependencia = tk.StringVar()
    filtro_autorizacion = tk.StringVar()
    filtro_valor = tk.StringVar()
    filtro_ObEspCon = tk.StringVar()
    filtro_consecutivo = tk.StringVar()
    filtro_id_version = tk.StringVar()
    filtro_id_comboObjeto = tk.StringVar()
    filtro_id_Obligaciones = tk.StringVar()

    def cargar_combo_data():
        try:
            # Tipo de Objeto
            sql = "SELECT nombre FROM obligacionesespecificas"
            db.cursor.execute(sql)
            obligaciones_especificas = db.cursor.fetchall()
            comboObligaciones['values'] = [row[0] for row in obligaciones_especificas]
            comboFiltroObligaciones_Específicas['values'] = comboObligaciones['values']  # También cargar en filtro

            # Tipo de Objeto
            sql = "SELECT nombreObjeto FROM objeto"
            db.cursor.execute(sql)
            objeto = db.cursor.fetchall()
            comboObjeto['values'] = [row[0] for row in objeto]
            comboFiltroTipoContrato['values'] = comboObjeto['values']  # También cargar en filtro
            
            # Tipo de Contrato
            sql = "SELECT nombreTipoContrato FROM tipodecontrato"
            db.cursor.execute(sql)
            tipodecontrato = db.cursor.fetchall()
            comboTipoContrato['values'] = [row[0] for row in tipodecontrato]
            comboFiltroTipoContrato['values'] = comboTipoContrato['values']  # También cargar en filtro

            # Cargo
            sql = "SELECT nombreCargo FROM cargo"
            db.cursor.execute(sql)
            cargos = db.cursor.fetchall()
            comboCargo['values'] = [row[0] for row in cargos]
            comboFiltroCargo['values'] = comboCargo['values']  # También cargar en filtro

            # Dependencia
            sql = "SELECT nombreDependencia FROM dependencia"
            db.cursor.execute(sql)
            dependencias = db.cursor.fetchall()
            comboDependencia['values'] = [row[0] for row in dependencias]
            comboFiltroDependencia['values'] = comboDependencia['values'] 

            # Clientes - Solo mostrar clientes activos
            sql = """
            SELECT clientes.id AS cliente_id, CONCAT_WS(' ', primerNombre, segundoNombre, primerApellido, segundoApellido) AS nombreCompleto 
            FROM clientes
            JOIN estado ON clientes.estado = estado.id
            WHERE estado.tipoEstado = 'activo'

            """
            db.cursor.execute(sql)
            clientes = db.cursor.fetchall()
            comboClientes['values'] = [row[1] for row in clientes]
            comboFiltroCliente['values'] = comboClientes['values']

        except Exception as e:
            print(f"Error al cargar datos en combobox: {e}")

    def limpiar_campos():
        id_independiente.set("")
        descripcion_contrato.set("")
        autorizacion_contratos.set("")
        valor_contrato.set("")
        comboObjeto.set("")
        obligaciones_especificas.set("")
        comboClientes.set("")
        comboTipoContrato.set("")
        comboCargo.set("")
        comboDependencia.set("")
        date_vigencia.set_date(datetime.today())
        date_terminacion.set_date(datetime.today())
        consecutivo.set("")
        comboObligaciones.set("")

    def llenar_tabla():
        print("Cargando datos en la tabla...")
        for item in tabla.get_children():
            tabla.delete(item)

        try:
            offset = (page_number - 1) * records_per_page
            # Base SQL query
            sql = """
            SELECT contrato.id, contrato.idVersion, clientes.id,
                CONCAT_WS(' ', clientes.primerNombre, clientes.segundoNombre, clientes.primerApellido, clientes.segundoApellido) AS nombreCompleto,
                tipodecontrato.nombreTipoContrato, cargo.nombreCargo, dependencia.nombreDependencia, objeto.nombreObjeto,
                contrato.descripcionContrato, contrato.Vigencia, contrato.terminacion, contrato.autorizacionContratos, contrato.valorContrato,
                obligacionesespecificas.nombre AS nombreObligacion, contrato.consecutivo
            FROM contrato
            JOIN clientes ON contrato.idClientes = clientes.id
            JOIN tipodecontrato ON contrato.idTipoContrato = tipodecontrato.id
            JOIN cargo ON contrato.idCargo = cargo.id
            JOIN dependencia ON contrato.idDependecia = dependencia.id
            JOIN objeto ON contrato.idObjeto = objeto.id
            JOIN obligacionesespecificas ON contrato.ObEspCon = obligacionesespecificas.id
            WHERE 1=1
            """

            
            valores = []

            # Aplicar filtros si se ingresaron valores
            if filtro_id_version.get():
                sql += " AND contrato.idVersion LIKE %s"
                valores.append(f"%{filtro_id_version.get()}%")
            if filtro_cliente.get():
                sql += " AND CONCAT_WS(' ', clientes.primerNombre, clientes.segundoNombre, clientes.primerApellido, clientes.segundoApellido) LIKE %s"
                valores.append(f"%{filtro_cliente.get()}%")
            if filtro_tipo_contrato.get():
                sql += " AND tipodecontrato.nombreTipoContrato LIKE %s"
                valores.append(f"%{filtro_tipo_contrato.get()}%")
            if filtro_cargo.get():
                sql += " AND cargo.nombreCargo LIKE %s"
                valores.append(f"%{filtro_cargo.get()}%")
            if filtro_dependencia.get():
                sql += " AND dependencia.nombreDependencia LIKE %s"
                valores.append(f"%{filtro_dependencia.get()}%")
                
            if filtro_autorizacion.get():
                sql += " AND contrato.autorizacionContratos LIKE %s"
                valores.append(f"%{filtro_autorizacion.get()}%")
            if filtro_valor.get():
                sql += " AND contrato.valorContrato LIKE %s"
                valores.append(f"%{filtro_valor.get()}%")

            # Agregar la paginación a la consulta
            sql += " LIMIT %s OFFSET %s"
            valores.extend([records_per_page, offset])

            db.cursor.execute(sql, valores)
            contratos = db.cursor.fetchall()
            print(f"Contratos obtenidos: {contratos}")

            for contrato in contratos:
                tabla.insert('', 'end', values=contrato)

        except Exception as e:  
            print(f"Error al llenar la tabla: {e}")

    def seleccionar_contrato(event):
        nonlocal modificar
        modificar = True

        selected_item = tabla.selection()
        if selected_item:
            item = tabla.item(selected_item)
            contrato = item['values']

            # Asignar valores a las variables usando .set() para cada StringVar
            id_independiente.set(contrato[0])
            id_version.set(contrato[1])
            comboClientes.set(contrato[3])
            comboTipoContrato.set(contrato[4])
            comboCargo.set(contrato[5])
            comboDependencia.set(contrato[6])
            comboObjeto.set(contrato[7])
            descripcion_contrato.set(contrato[8])
            date_vigencia.set_date(contrato[9])
            date_terminacion.set_date(contrato[10])
            autorizacion_contratos.set(contrato[11])
            valor_contrato.set(contrato[12])
            comboObligaciones.set(contrato[13])
            consecutivo.set(contrato[14])


    def guardar_contrato():
        if modificar:
            actualizar_contrato()
        else:
            insertar_contrato()

    def insertar_contrato():
        try:
            if not date_vigencia.get_date() or not date_terminacion.get_date():
                print("Error: Las fechas de vigencia y terminación son obligatorias.")
                return

            # Obtener los IDs necesarios para la inserción
            sql_cliente = """
            SELECT id FROM clientes 
            WHERE CONCAT_WS(' ', primerNombre, segundoNombre, primerApellido, segundoApellido) = %s
            LIMIT 1
            """
            db.cursor.execute(sql_cliente, (comboClientes.get(),))
            cliente_id = db.cursor.fetchone()

            sql_tipo_contrato = """
            SELECT id FROM tipodecontrato 
            WHERE nombreTipoContrato = %s
            LIMIT 1
            """
            db.cursor.execute(sql_tipo_contrato, (comboTipoContrato.get(),))
            tipo_contrato_id = db.cursor.fetchone()

            sql_cargo = """
            SELECT id FROM cargo 
            WHERE nombreCargo = %s
            LIMIT 1
            """
            db.cursor.execute(sql_cargo, (comboCargo.get(),))
            cargo_id = db.cursor.fetchone()

            sql_dependencia = """
            SELECT id FROM dependencia 
            WHERE nombreDependencia = %s
            LIMIT 1
            """
            db.cursor.execute(sql_dependencia, (comboDependencia.get(),))
            dependencia_id = db.cursor.fetchone()

            sql_objeto = """
            SELECT id FROM objeto    
            WHERE nombreObjeto = %s
            LIMIT 1
            """
            db.cursor.execute(sql_objeto, (comboObjeto.get(),))
            objeto_id = db.cursor.fetchone()

            sql_ObEspCon = """
            SELECT id FROM obligacionesespecificas    
            WHERE nombre = %s
            LIMIT 1
            """
            db.cursor.execute(sql_ObEspCon, (comboObligaciones.get(),))
            obligaciones_especificas = db.cursor.fetchone()

            # Validar que todos los IDs se hayan encontrado
            if cliente_id and tipo_contrato_id and cargo_id and dependencia_id and objeto_id and obligaciones_especificas:
                # Insertar el contrato sin `idVersion`
                sql_insert = """
                INSERT INTO contrato 
                (idClientes, idTipoContrato, idCargo, idDependecia, idObjeto, descripcionContrato, Vigencia, terminacion, autorizacionContratos, valorContrato, ObEspCon, consecutivo) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (
                    cliente_id[0],
                    tipo_contrato_id[0],
                    cargo_id[0],
                    dependencia_id[0],
                    objeto_id[0],
                    descripcion_contrato.get(),
                    date_vigencia.get_date(),
                    date_terminacion.get_date(),
                    autorizacion_contratos.get(),
                    valor_contrato.get(),
                    obligaciones_especificas[0],  # Acceder al ID desde la tupla
                    consecutivo.get()  # Consecutivo
                )
                db.cursor.execute(sql_insert, valores)
                db.cursor.connection.commit()

                # Obtener el ID del registro recién insertado
                contrato_id = db.cursor.lastrowid

                # Crear el valor para `idVersion` como `id-1`
                id_version = f"{contrato_id}-1"

                # Actualizar el registro con `idVersion`
                sql_update_version = """
                UPDATE contrato
                SET idVersion = %s
                WHERE id = %s
                """
                db.cursor.execute(sql_update_version, (id_version, contrato_id))
                db.cursor.connection.commit()

                limpiar_campos()
                llenar_tabla()
            else:
                print("Error: No se encontraron todos los IDs requeridos.")

        except Exception as e:
            print(f"Error al insertar contrato: {e}")
            db.cursor.connection.rollback()

    def actualizar_contrato():
        try:
            selected_item = tabla.selection()
            if selected_item:
                item = tabla.item(selected_item)
                contrato_id = item['values'][0]

                # Obtener los IDs necesarios para la actualización
                sql_cliente = """
                SELECT id FROM clientes 
                WHERE CONCAT_WS(' ', primerNombre, segundoNombre, primerApellido, segundoApellido) = %s
                LIMIT 1
                """
                db.cursor.execute(sql_cliente, (comboClientes.get(),))
                cliente_id = db.cursor.fetchone()

                sql_tipo_contrato = """
                SELECT id FROM tipodecontrato 
                WHERE nombreTipoContrato = %s
                LIMIT 1
                """
                db.cursor.execute(sql_tipo_contrato, (comboTipoContrato.get(),))
                tipo_contrato_id = db.cursor.fetchone()

                sql_cargo = """
                SELECT id FROM cargo 
                WHERE nombreCargo = %s
                LIMIT 1
                """
                db.cursor.execute(sql_cargo, (comboCargo.get(),))
                cargo_id = db.cursor.fetchone()

                sql_dependencia = """
                SELECT id FROM dependencia 
                WHERE nombreDependencia = %s
                LIMIT 1
                """
                db.cursor.execute(sql_dependencia, (comboDependencia.get(),))
                dependencia_id = db.cursor.fetchone()

                sql_obligaciones_especificas = """
                SELECT id FROM obligacionesespecificas
                WHERE nombre = %s
                LIMIT 1
                """
                db.cursor.execute(sql_obligaciones_especificas, (comboObligaciones.get(),))
                obligaciones_especificas_id = db.cursor.fetchone()

                # Imprimir el valor del comboObjeto
                objeto_nombre = comboObjeto.get()
                print(f"Valor de objeto: {objeto_nombre}")

                sql_objeto = """
                SELECT id FROM objeto
                WHERE nombreObjeto = %s
                LIMIT 1
                """
                db.cursor.execute(sql_objeto, (objeto_nombre,))
                objeto_id = db.cursor.fetchone()

                # Validar que todos los IDs se hayan encontrado
                if cliente_id and tipo_contrato_id and cargo_id and dependencia_id and obligaciones_especificas_id and objeto_id:
                    sql_update = """
                    UPDATE contrato 
                    SET idClientes = %s,
                        idTipoContrato = %s,
                        idCargo = %s,
                        idDependecia = %s,
                        idObjeto = %s,
                        descripcionContrato = %s, 
                        Vigencia = %s,
                        terminacion = %s,
                        autorizacionContratos = %s, 
                        valorContrato = %s,
                        ObEspCon = %s,
                        consecutivo = %s
                    WHERE id = %s
                    """
                    valores = (
                        cliente_id[0],
                        tipo_contrato_id[0],
                        cargo_id[0],
                        dependencia_id[0],
                        objeto_id[0],
                        descripcion_contrato.get(),
                        date_vigencia.get_date(),
                        date_terminacion.get_date(),
                        autorizacion_contratos.get(),
                        valor_contrato.get(),
                        obligaciones_especificas_id[0],
                        consecutivo.get(),
                        contrato_id
                    )
                    db.cursor.execute(sql_update, valores)
                    db.cursor.connection.commit()

                    limpiar_campos()
                    llenar_tabla()
                else:
                    print("Error: No se encontraron todos los IDs requeridos.")
                    if not cliente_id:
                        print(f"No se encontró un cliente con el nombre: {comboClientes.get()}")
                    if not tipo_contrato_id:
                        print(f"No se encontró un tipo de contrato con el nombre: {comboTipoContrato.get()}")
                    if not cargo_id:
                        print(f"No se encontró un cargo con el nombre: {comboCargo.get()}")
                    if not dependencia_id:
                        print(f"No se encontró una dependencia con el nombre: {comboDependencia.get()}")
                    if not obligaciones_especificas_id:
                        print(f"No se encontró una obligación específica con el nombre: {comboObligaciones.get()}")
                    if not objeto_id:
                        print(f"No se encontró un objeto con el nombre: {objeto_nombre}")

        except Exception as e:
            print(f"Error al actualizar contrato: {e}")
            db.cursor.connection.rollback()

    def eliminar_contrato():
        try:
            selected_item = tabla.selection()
            if selected_item:
                item = tabla.item(selected_item)
                contrato_id = item['values'][0]

                # Obtener un bloqueo sobre el registro antes de eliminar
                db.cursor.execute("SELECT * FROM contrato WHERE id = %s FOR UPDATE", (contrato_id,))

                # Eliminar el contrato
                sql = "DELETE FROM contrato WHERE id = %s"
                db.cursor.execute(sql, (contrato_id,))
                db.cursor.connection.commit()

                limpiar_campos()
                llenar_tabla()
                print("Contrato eliminado exitosamente")

        except Exception as e:
            print(f"Error al eliminar contrato: {e}")
            db.cursor.connection.rollback()

    def ir_a_pagina_anterior():
        nonlocal page_number
        if page_number > 1:
            page_number -= 1
            llenar_tabla()
            actualizar_botones_paginacion()

    def ir_a_pagina_siguiente():
        nonlocal page_number
        page_number += 1
        llenar_tabla()
        actualizar_botones_paginacion()

    def mostrar_todos_los_registros():
        filtro_cliente.set("")
        filtro_tipo_contrato.set("")
        filtro_cargo.set("")
        filtro_dependencia.set("")
        filtro_id_comboObjeto.set("")
        filtro_autorizacion.set("")
        filtro_valor.set("")
        filtro_ObEspCon.set("")
        filtro_consecutivo.set("")
        filtro_id_version.set("")
        llenar_tabla()

    def actualizar_botones_paginacion():
        btnAnterior.config(state=tk.NORMAL if page_number > 1 else tk.DISABLED)

    # Función para abrir una nueva pantalla que permita ver la barra de Windows
    def abrir_nueva_pantalla():
        nueva_pantalla = tk.Toplevel()
        nueva_pantalla.title("Nueva pantalla")
        
        # Adaptar la nueva pantalla al tamaño de la pantalla, pero permitiendo ver la barra de tareas
        screen_width = pantalla.winfo_screenwidth()
        screen_height = pantalla.winfo_screenheight() - 50  # Dejar espacio para la barra de Windows
        nueva_pantalla.geometry(f"{screen_width}x{screen_height}+0+0")  # Colocar en la esquina superior izquierda

        # Crear un marco para los botones minimizar y cerrar
        botones_marco = tk.Frame(nueva_pantalla)
        botones_marco.pack(pady=10)

        # Botón minimizar (amarillo)
        minimizar_btn = tk.Button(botones_marco, text="—", command=nueva_pantalla.iconify, bg="yellow", fg="black", font=("Helvetica", 14), width=5)
        minimizar_btn.grid(row=0, column=0, padx=5)

        # Botón cerrar (rojo)
        cerrar_btn = tk.Button(botones_marco, text="X", command=nueva_pantalla.destroy, bg="red", fg="white", font=("Helvetica", 14), width=5)
        cerrar_btn.grid(row=0, column=1, padx=5)
    
    # Crear el marco dentro de la pantalla principal
    marco = tk.Frame(frame)
    marco.pack(fill='both', expand=True)

    # Definir la fuente para el título h1
    font_h1 = font.Font(family="Helvetica", size=20, weight="bold")

    # Crear la etiqueta que simula un título h1
    label_h1 = tk.Label(marco, text="Contrataciones", font=font_h1)
    label_h1.pack(pady=3)

    # Crear un marco para organizar los botones debajo del título
    marco_botones = tk.Frame(marco)
    marco_botones.pack(pady=3)
    # Contenedor para los formularios y la tabla
    contenedor_formulario = tk.Frame(marco)
    contenedor_formulario.pack(fill='x', padx=10, pady=10)

    contenedor_fila_id = tk.Frame(contenedor_formulario)
    contenedor_fila_id.pack(fill='x', pady=5)
    # Validación para asegurarse de que el input sea numérico
    def solo_numeros(texto):
        return texto.isdigit()

    validacion_numerica = frame.register(solo_numeros)
    db = DataBase()
    # Crear la conexión a la base de datos y obtener nombres de objetos
    try:
        db = DataBase()
        nombres_objetos = db.obtener_nombres_objetos()
        print("Contratos obtenidos:", nombres_objetos)
    except Exception as e:
        print(f"Error al obtener nombres de objetos: {e}")
        nombres_objetos = []  # Asigna una lista vacía en caso de error
    
    db = DataBase()
    # Crear la conexión a la base de datos y obtener nombres de objetos
    try:
        db = DataBase()
        nombres_obligaciones_especificas= db.obtener_nombres_obligaciones_especificas()
        print("Contratos obtenidos:", nombres_obligaciones_especificas)
    except Exception as e:
        print(f"Error al obtener nombres de obligaciones especificas: {e}")
        nombres_obligaciones_especificas = []  # Asigna una lista vacía en caso de error

    def abrir_objeto_window():
        # Crear una nueva pantalla para "Objeto"
        pantalla_objeto = tk.Toplevel()
        pantalla_objeto.title("CRUD Objeto")

        # Inicializar variables
        db = DataBase()
        global page_number, records_per_page, total_records
        page_number = 1
        records_per_page = 10
        total_records = 0

        id_objeto = tk.StringVar()
        nombre_objeto = tk.StringVar()
        filtro_nombre = tk.StringVar()

        def aplicar_filtro(*args):
            llenar_tabla()

        def seleccionar(event):
            # Actualizar el campo de texto con el registro seleccionado
            seleccion = tvObjetos.selection()
            if seleccion:
                id = seleccion[0]
                valores = tvObjetos.item(id, "values")
                id_objeto.set(valores[0])
                nombre_objeto.set(valores[1])

        def eliminar():
            seleccion = tvObjetos.selection()
            if seleccion:
                id = seleccion[0]
                if int(id) > 0:
                    sql = "DELETE FROM objeto WHERE id=%s"
                    try:
                        db.cursor.execute(sql, (id,))
                        db.connection.commit()
                        tvObjetos.delete(id)
                        lblMensaje.config(text="Se ha eliminado el registro correctamente", fg="green")
                        limpiar()
                        llenar_tabla()  # Actualizar tabla después de eliminar
                    except pymysql.MySQLError as e:
                        lblMensaje.config(text=f"Error al eliminar el registro: {e}", fg="red")
                else:
                    lblMensaje.config(text="Seleccione un registro para eliminar", fg="red")

        def nuevo():
            if validar():
                if id_objeto.get() == "":  # Si no hay ID, es un nuevo registro
                    # Obtener el siguiente ID auto-incremental
                    sql_get_id = "SELECT IFNULL(MAX(id), 0) + 1 FROM objeto"
                    db.cursor.execute(sql_get_id)
                    nuevo_id = db.cursor.fetchone()[0]

                    sql = "INSERT INTO objeto (id, nombreObjeto) VALUES (%s, %s)"
                    try:
                        db.cursor.execute(sql, (nuevo_id, nombre_objeto.get()))
                        db.connection.commit()
                        lblMensaje.config(text="Se ha guardado el registro con éxito", fg="green")
                        llenar_tabla()
                        limpiar()
                    except pymysql.MySQLError as e:
                        lblMensaje.config(text=f"Error al guardar el registro: {e}", fg="red")
                else:  # Si hay ID, es una actualización
                    actualizar()
            else:
                lblMensaje.config(text="Los campos no deben estar vacíos", fg="red")

        def actualizar():
            if validar():
                id = id_objeto.get()  # Tomar el ID del campo de texto
                if id:
                    sql = "UPDATE objeto SET nombreObjeto=%s WHERE id=%s"
                    try:
                        db.cursor.execute(sql, (nombre_objeto.get(), id))
                        db.connection.commit()
                        lblMensaje.config(text="Se ha actualizado el registro con éxito", fg="green")
                        llenar_tabla()
                        limpiar()
                    except pymysql.MySQLError as e:
                        lblMensaje.config(text=f"Error al actualizar el registro: {e}", fg="red")

        def limpiar():
            id_objeto.set("")
            nombre_objeto.set("")
            filtro_nombre.set("")

        def validar():
            return len(nombre_objeto.get()) > 0

        def vaciar_tabla():
            filas = tvObjetos.get_children()
            for fila in filas:
                tvObjetos.delete(fila)

        def llenar_tabla():
            vaciar_tabla()
            global total_records
            offset = (page_number - 1) * records_per_page
            sql_count = "SELECT COUNT(*) FROM objeto WHERE nombreObjeto LIKE %s"
            try:
                db.cursor.execute(sql_count, ('%' + filtro_nombre.get() + '%',))
                total_records = db.cursor.fetchone()[0]

                sql = "SELECT id, nombreObjeto FROM objeto WHERE nombreObjeto LIKE %s LIMIT %s OFFSET %s"
                db.cursor.execute(sql, ('%' + filtro_nombre.get() + '%', records_per_page, offset))
                filas = db.cursor.fetchall()
                for fila in filas:
                    id = fila[0]
                    tvObjetos.insert("", 'end', id, text=id, values=(fila[0], fila[1]))
            except pymysql.MySQLError as e:
                lblMensaje.config(text=f"Error al cargar datos: {e}", fg="red")
            # Actualizar el estado de los botones de navegación
            btnPrev.config(state='normal' if page_number > 1 else 'disabled')
            btnNext.config(state='normal' if page_number * records_per_page < total_records else 'disabled')

        def paginacion():
            llenar_tabla()
            # Actualizar el estado de los botones de navegación
            btnPrev.config(state='normal' if page_number > 1 else 'disabled')
            btnNext.config(state='normal' if page_number * records_per_page < total_records else 'disabled')

        def prev_page():
            global page_number
            if page_number > 1:
                page_number -= 1
                paginacion()

        def next_page():
            global page_number
            if page_number * records_per_page < total_records:
                page_number += 1
                paginacion()

        # Crear el marco de la pantalla
        marco = tk.LabelFrame(pantalla_objeto, text="Formulario Objeto")
        marco.place(x=50, y=50, width=1500, height=1400)

        # Botones para cerrar y minimizar
        btnCerrar = tk.Button(marco, text="X", command=pantalla_objeto.destroy, bg="red", fg="white")
        btnCerrar.place(x=470, y=10, width=20, height=20)

        btnMinimizar = tk.Button(marco, text="-", command=lambda: pantalla_objeto.iconify(), bg="yellow", fg="black")
        btnMinimizar.place(x=450, y=10, width=20, height=20)

        tk.Label(marco, text="ID").grid(column=0, row=0, padx=5, pady=5)
        txtIdObjeto = tk.Entry(marco, textvariable=id_objeto, state='disabled')
        txtIdObjeto.grid(column=1, row=0)

        tk.Label(marco, text="Nombre").grid(column=0, row=1, padx=5, pady=5)
        txtNombreObjeto = tk.Entry(marco, textvariable=nombre_objeto)
        txtNombreObjeto.grid(column=1, row=1)

        tk.Label(marco, text="Filtro Nombre").grid(column=0, row=2, padx=5, pady=5)
        txtFiltroNombre = tk.Entry(marco, textvariable=filtro_nombre)
        txtFiltroNombre.grid(column=1, row=2)
        filtro_nombre.trace_add('write', aplicar_filtro)

        lblMensaje = tk.Label(marco, text="Aquí van los mensajes", fg="green")
        lblMensaje.grid(column=0, row=3, columnspan=4)

        tvObjetos = ttk.Treeview(marco, selectmode='browse')  # Cambiar a modo 'browse'
        tvObjetos["columns"] = ("ID", "Nombre")
        tvObjetos.column("#0", width=0, stretch='no')
        tvObjetos.column("ID", width=150, anchor='center')
        tvObjetos.column("Nombre", width=150, anchor='center')
        tvObjetos.heading("#0", text="")
        tvObjetos.heading("ID", text="ID", anchor='center')
        tvObjetos.heading("Nombre", text="Nombre", anchor='center')
        tvObjetos.grid(column=0, row=4, columnspan=4, padx=5)
        tvObjetos.bind("<<TreeviewSelect>>", seleccionar)

        # Botones de acción
        btnEliminar = tk.Button(marco, text="Eliminar", command=eliminar)
        btnEliminar.grid(column=1, row=6, padx=5, pady=10)

        btnNuevo = tk.Button(marco, text="Guardar", command=nuevo)
        btnNuevo.grid(column=2, row=6, padx=5, pady=10)

        btnActualizar = tk.Button(marco, text="Actualizar", command=actualizar)
        btnActualizar.grid(column=3, row=6, padx=5, pady=10)

        btnLimpiar = tk.Button(marco, text="Limpiar", command=limpiar)
        btnLimpiar.grid(column=0, row=6, padx=5, pady=10)

        # Botones de navegación
        btnPrev = tk.Button(marco, text="<< Anterior", command=prev_page)
        btnPrev.grid(column=0, row=7, pady=10, sticky='w')

        btnNext = tk.Button(marco, text="Siguiente >>", command=next_page)
        btnNext.grid(column=3, row=7, pady=10, sticky='e')

        llenar_tabla()

    def abrir_obligaciones_window():
        # Crear una nueva pantalla para "Obligaciones Específicas"
        pantalla_obligaciones = tk.Toplevel()
        pantalla_obligaciones.title("CRUD Obligaciones Específicas")

        # Inicializar variables
        db = DataBase()
        global page_number, records_per_page, total_records
        page_number = 1
        records_per_page = 10
        total_records = 0

        modificar = False
        id_obligacion = tk.StringVar()
        nombre_obligacion = tk.StringVar()
        id_objeto = tk.StringVar()
        año = tk.StringVar()
        filtro_nombre = tk.StringVar()
        filtro_año = tk.StringVar()
        filtro_id_objeto = tk.StringVar()

        def aplicar_filtro(*args):
            llenar_tabla()

        def seleccionar(event):
            seleccion = tvObligaciones.selection()
            if seleccion:
                id = seleccion[0]
                valores = tvObligaciones.item(id, "values")
                id_obligacion.set(valores[0])
                nombre_obligacion.set(valores[1])
                id_objeto.set(valores[2])
                año.set(valores[3])
                btnEliminar.config(state='normal')

        def eliminar():
            seleccion = tvObligaciones.selection()
            if seleccion:
                id = seleccion[0]
                if int(id) > 0:
                    sql = "DELETE FROM obligacionesespecificas WHERE id=%s"
                    try:
                        db.cursor.execute(sql, (id,))
                        db.connection.commit()
                        tvObligaciones.delete(id)
                        lblMensaje.config(text="Se ha eliminado el registro correctamente", fg="green")
                        limpiar()
                        llenar_tabla()
                    except pymysql.MySQLError as e:
                        lblMensaje.config(text=f"Error al eliminar el registro: {e}", fg="red")
                else:
                    lblMensaje.config(text="Seleccione un registro para eliminar", fg="red")

        def nuevo():
            if not modificar:
                if validar():
                    sql_get_id = "SELECT IFNULL(MAX(id), 0) + 1 FROM obligacionesespecificas"
                    db.cursor.execute(sql_get_id)
                    nuevo_id = db.cursor.fetchone()[0]

                    sql = "INSERT INTO obligacionesespecificas (id, nombre, idObjeto, año) VALUES (%s, %s, %s, %s)"
                    try:
                        db.cursor.execute(sql, (nuevo_id, nombre_obligacion.get(), id_objeto.get(), año.get()))
                        db.connection.commit()
                        lblMensaje.config(text="Se ha guardado el registro con éxito", fg="green")
                        llenar_tabla()
                        limpiar()
                    except pymysql.MySQLError as e:
                        lblMensaje.config(text=f"Error al guardar el registro: {e}", fg="red")
                else:
                    lblMensaje.config(text="Los campos no deben estar vacíos", fg="red")
            else:
                modificarFalse()

        def actualizar():
            if modificar:
                if validar():
                    id = id_obligacion.get()
                    if id:
                        sql = "UPDATE obligacionesespecificas SET nombre=%s, idObjeto=%s, año=%s WHERE id=%s"
                        try:
                            db.cursor.execute(sql, (nombre_obligacion.get(), id_objeto.get(), año.get(), id))
                            db.connection.commit()
                            lblMensaje.config(text="Se ha guardado el registro con éxito", fg="green")
                            llenar_tabla()
                            limpiar()
                        except pymysql.MySQLError as e:
                            lblMensaje.config(text=f"Error al actualizar el registro: {e}", fg="red")
                else:
                    lblMensaje.config(text="Los campos no deben estar vacíos", fg="red")
            else:
                modificarTrue()

        def vaciar_tabla():
            filas = tvObligaciones.get_children()
            for fila in filas:
                tvObligaciones.delete(fila)

        def llenar_tabla():
            vaciar_tabla()
            global total_records
            offset = (page_number - 1) * records_per_page

            sql_count = """
            SELECT COUNT(*) 
            FROM obligacionesespecificas o 
            LEFT JOIN objeto ob ON o.idObjeto = ob.id 
            WHERE o.nombre LIKE %s 
            AND o.año LIKE %s 
            """
            try:
                db.cursor.execute(sql_count, ('%' + filtro_nombre.get() + '%', '%' + filtro_año.get() + '%'))
                total_records = db.cursor.fetchone()[0]

                sql = """
                SELECT o.id, o.nombre, ob.nombreObjeto, o.año 
                FROM obligacionesespecificas o 
                LEFT JOIN objeto ob ON o.idObjeto = ob.id 
                WHERE o.nombre LIKE %s 
                AND o.año LIKE %s 
                LIMIT %s OFFSET %s
                """
                db.cursor.execute(sql, ('%' + filtro_nombre.get() + '%', '%' + filtro_año.get() + '%', records_per_page, offset))
                filas = db.cursor.fetchall()
                for fila in filas:
                    id = fila[0]
                    tvObligaciones.insert("", 'end', id, text=id, values=(fila[0], fila[1], fila[2] if fila[2] else 'None', fila[3]))
            except pymysql.MySQLError as e:
                lblMensaje.config(text=f"Error al cargar datos: {e}", fg="red")
            
            btnPrev.config(state='normal' if page_number > 1 else 'disabled')
            btnNext.config(state='normal' if page_number * records_per_page < total_records else 'disabled')

        def limpiar():
            id_obligacion.set("")
            nombre_obligacion.set("")
            id_objeto.set("")
            año.set("")
            btnEliminar.config(state='disabled')

        def validar():
            return (len(nombre_obligacion.get()) > 0 and 
                    len(id_objeto.get()) > 0 and 
                    len(año.get()) > 0)

        def modificarFalse():
            nonlocal modificar
            modificar = False
            tvObligaciones.config(selectmode='none')
            btnNuevo.config(text="Guardar")
            btnActualizar.config(text="Actualizar")
            btnEliminar.config(state='disabled')

        def modificarTrue():
            nonlocal modificar
            modificar = True
            tvObligaciones.config(selectmode='browse')
            btnNuevo.config(text="Nuevo")
            btnActualizar.config(text="Actualizar")
            btnEliminar.config(state='normal')

        def paginacion():
            llenar_tabla()
            btnPrev.config(state='normal' if page_number > 1 else 'disabled')
            btnNext.config(state='normal' if page_number * records_per_page < total_records else 'disabled')

        def prev_page():
            global page_number
            if page_number > 1:
                page_number -= 1
                paginacion()

        def next_page():
            global page_number
            if page_number * records_per_page < total_records:
                page_number += 1
                paginacion()

        def cargar_objetos():
            sql = "SELECT id, nombreObjeto FROM objeto"
            try:
                db.cursor.execute(sql)
                objetos = db.cursor.fetchall()
                comboIdObjeto['values'] = [obj[1] for obj in objetos]
            except pymysql.MySQLError as e:
                lblMensaje.config(text=f"Error al cargar objetos: {e}", fg="red")

        # Crear el marco de la pantalla
        marco = tk.LabelFrame(pantalla_obligaciones, text="Formulario Obligaciones Específicas")
        marco.place(x=50, y=50, width=1500, height=700)

        # Botones para cerrar y minimizar
        btnCerrar = tk.Button(marco, text="X", command=pantalla_obligaciones.destroy, bg="red", fg="white")
        btnCerrar.place(x=470, y=10, width=20, height=20)

        btnMinimizar = tk.Button(marco, text="-", command=lambda: pantalla_obligaciones.iconify(), bg="yellow", fg="black")
        btnMinimizar.place(x=450, y=10, width=20, height=20)

        # Crear marco para la sección de registro
        marco_registro = tk.Frame(marco)
        marco_registro.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas y campos de entrada
        tk.Label(marco_registro, text="ID Obligación").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(marco_registro, textvariable=id_obligacion, state='disabled').grid(row=0, column=1, padx=5, pady=5)

        tk.Label(marco_registro, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(marco_registro, textvariable=nombre_obligacion).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(marco_registro, text="ID Objeto").grid(row=2, column=0, padx=5, pady=5)

        comboIdObjeto = ttk.Combobox(marco_registro, textvariable=id_objeto)
        comboIdObjeto.grid(row=2, column=1, padx=5, pady=5)
        comboIdObjeto.bind("<<ComboboxSelected>>", lambda e: id_objeto.set(comboIdObjeto.get()))
        cargar_objetos()

        tk.Label(marco_registro, text="Año").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(marco_registro, textvariable=año).grid(row=3, column=1, padx=5, pady=5)

        # Botones para guardar, actualizar y eliminar
        btnNuevo = tk.Button(marco_registro, text="Guardar", command=nuevo)
        btnNuevo.grid(row=4, column=0, padx=5, pady=5)

        btnActualizar = tk.Button(marco_registro, text="Actualizar", command=actualizar)
        btnActualizar.grid(row=4, column=1, padx=5, pady=5)

        btnEliminar = tk.Button(marco_registro, text="Eliminar", command=eliminar, state='disabled')
        btnEliminar.grid(row=4, column=2, padx=5, pady=5)

        # Mensaje
        lblMensaje = tk.Label(marco_registro, text="", fg="red")
        lblMensaje.grid(row=5, column=0, columnspan=3)

        # Crear marco para la sección de filtros
        marco_filtros = tk.Frame(marco)
        marco_filtros.grid(row=0, column=1, padx=10, pady=10)

        # Etiquetas y campos de filtro
        tk.Label(marco_filtros, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(marco_filtros, textvariable=filtro_nombre).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(marco_filtros, text="Año").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(marco_filtros, textvariable=filtro_año).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(marco_filtros, text="ID Objeto").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(marco_filtros, textvariable=filtro_id_objeto).grid(row=2, column=1, padx=5, pady=5)

        # Botón para aplicar filtro
        btnFiltrar = tk.Button(marco_filtros, text="Filtrar", command=aplicar_filtro)
        btnFiltrar.grid(row=3, column=0, columnspan=2)

        # Crear la tabla
        columnas = ("ID", "Nombre", "ID Objeto", "Año")
        tvObligaciones = ttk.Treeview(marco, columns=columnas, show="headings")
        tvObligaciones.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        for col in columnas:
            tvObligaciones.heading(col, text=col)

        tvObligaciones.bind("<ButtonRelease-1>", seleccionar)

        # Crear botones de paginación
        btnPrev = tk.Button(marco, text="<<", command=prev_page)
        btnPrev.grid(row=2, column=0, sticky='w')

        btnNext = tk.Button(marco, text=">>", command=next_page)
        btnNext.grid(row=2, column=1, sticky='e')

        # Llenar tabla inicialmente
        llenar_tabla()

    def validar_numeros(char):
        return char.isdigit()  # Permitir solo caracteres numéricos
    # Función para obtener objetos desde la base de datos
    def obtener_objetos():
        try:
            # Conexión a la base de datos
            conexion = pymysql.connect(host='localhost', user='root', password='', db='contrataciones')
            cursor = conexion.cursor()

            # Consulta SQL para obtener los nombres de los objetos
            cursor.execute("SELECT nombre FROM objetos")
            resultados = cursor.fetchall()

            # Extraer los nombres de los objetos y almacenarlos en una lista
            nombres_objetos = [fila[0] for fila in resultados]

            conexion.close()  # Cerrar la conexión

            return nombres_objetos

        except Exception as e:
            print(f"Error al obtener objetos: {e}")
            return []

    # Cargar los nombres de objetos en la variable
    nombres_objetos = obtener_objetos()
    # Función para obtener las obligaciones específicas desde la base de datos
    def obtener_obligaciones_especificas():
        try:
            # Conexión a la base de datos
            conexion = pymysql.connect(host='localhost', user='root', password='', db='contrataciones')
            cursor = conexion.cursor()

            # Consulta SQL para obtener las obligaciones específicas
            cursor.execute("SELECT nombre FROM obligaciones_especificas")
            resultados = cursor.fetchall()

            # Extraer los nombres de las obligaciones y almacenarlos en una lista
            nombres_obligaciones_especificas = [fila[0] for fila in resultados]

            conexion.close()  # Cerrar la conexión

            return nombres_obligaciones_especificas

        except Exception as e:
            print(f"Error al obtener obligaciones específicas: {e}")
            return []

    # Cargar los nombres de obligaciones en la variable
    nombres_obligaciones_especificas = obtener_obligaciones_especificas()
    # Crear el validador numérico
    validacion_numerica = contenedor_formulario.register(validar_numeros)

    # Filas para organizar los inputs y selects
    for i in range(5):  # Cambiar el rango a 5 para incluir la fila adicional para "Objeto"
        contenedor_fila = tk.Frame(contenedor_formulario)
        contenedor_fila.pack(fill='x', pady=5)
        if i == 0:
            # Fila 1
            tk.Label(contenedor_fila, text="ID Independiente:").grid(row=0, column=0, sticky="e")
            entry_id_independiente = tk.Entry(contenedor_fila, textvariable=id_independiente, state='readonly')
            entry_id_independiente.grid(row=0, column=1, sticky="ew")

            # Alineando los siguientes elementos en la misma fila
            tk.Label(contenedor_fila, text="Cliente:").grid(row=0, column=2, sticky="e")
            comboClientes = ttk.Combobox(contenedor_fila)
            comboClientes.grid(row=0, column=3, sticky="ew")

            tk.Label(contenedor_fila, text="Tipo de Contrato:").grid(row=0, column=4, sticky="e")
            comboTipoContrato = ttk.Combobox(contenedor_fila)
            comboTipoContrato.grid(row=0, column=5, sticky="ew")

            tk.Label(contenedor_fila, text="Cargo:").grid(row=0, column=6, sticky="e")
            comboCargo = ttk.Combobox(contenedor_fila)
            comboCargo.grid(row=0, column=7, sticky="ew")

            tk.Label(contenedor_fila, text="Dependencia:").grid(row=0, column=8, sticky="e")
            comboDependencia = ttk.Combobox(contenedor_fila)
            comboDependencia.grid(row=0, column=9, sticky="ew")


        elif i == 1:
            # Fila 1 - Descripción y otros elementos
            tk.Label(contenedor_fila, text="Descripción:").grid(row=1, column=0, sticky="e")
            tk.Entry(contenedor_fila, textvariable=descripcion_contrato).grid(row=1, column=1, sticky="ew")

            tk.Label(contenedor_fila, text="Vigencia:").grid(row=1, column=2, sticky="e")
            date_vigencia = DateEntry(contenedor_fila, width=20, background='darkblue',
                                    foreground='white', borderwidth=2, date_pattern='y-mm-dd')
            date_vigencia.grid(row=1, column=3, sticky="ew")

            tk.Label(contenedor_fila, text="Terminación:").grid(row=1, column=4, sticky="e")
            date_terminacion = DateEntry(contenedor_fila, width=20, background='darkblue',
                                        foreground='white', borderwidth=2, date_pattern='y-mm-dd')
            date_terminacion.grid(row=1, column=5, sticky="ew")

            # Fila 2 - Autorización y Valor (se alinean en la misma fila)
            tk.Label(contenedor_fila, text="Autorización:").grid(row=1, column=6, sticky="e")
            tk.Entry(contenedor_fila, textvariable=autorizacion_contratos, validate="key", 
                    validatecommand=(validacion_numerica, '%S')).grid(row=1, column=7, sticky="ew")

            tk.Label(contenedor_fila, text="Valor:").grid(row=1, column=8, sticky="e")
            tk.Entry(contenedor_fila, textvariable=valor_contrato, validate="key", 
                    validatecommand=(validacion_numerica, '%S')).grid(row=1, column=9, sticky="ew")


        elif i == 2:  # Nueva fila para "Objeto"
            tk.Label(contenedor_fila, text="Objeto:").grid(row=0, column=0, sticky="e")
            comboObjeto = ttk.Combobox(contenedor_fila, textvariable=id_version, values=nombres_objetos, width=40)  # Adjust 'width' to desired value
            comboObjeto.grid(row=0, column=1, sticky="ew", ipady=5)
            comboObjeto.bind("<KeyRelease>", obtener_objetos)  # Filtrar mientras escribes

            tk.Label(contenedor_fila, text="Obligaciones Específicas:").grid(row=0, column=2, sticky="e")
            comboObligaciones = ttk.Combobox(contenedor_fila, textvariable=obligaciones_especificas, values=nombres_obligaciones_especificas, width=40,  justify="left")
            comboObligaciones.grid(row=0, column=3, columnspan=3, sticky="ew", ipady=5)
            comboObligaciones.bind("<KeyRelease>", obtener_obligaciones_especificas)  # Filtrar mientras escribes

            tk.Label(contenedor_fila, text="Consecutivo:").grid(row=0, column=6, sticky="e")
            entry_consecutivo = tk.Entry(contenedor_fila, textvariable=consecutivo, validate="key", 
                                        validatecommand=(validacion_numerica, '%S'))
            entry_consecutivo.grid(row=0, column=7, sticky="ew")

            tk.Label(contenedor_fila, text="Consecutivo:").grid(row=0, column=6, sticky="e")
            entry_consecutivo = tk.Entry(contenedor_fila, textvariable=consecutivo, validate="key", 
                                        validatecommand=(validacion_numerica, '%S'))
            entry_consecutivo.grid(row=0, column=7, sticky="ew")

            # Botón para crear nuevo objeto
            tk.Button(contenedor_fila, text="Crear Objeto", command=abrir_objeto_window).grid(row=0, column=8, padx=5)

            # Botón para crear nuevas obligaciones específicas
            tk.Button(contenedor_fila, text="Crear Obligaciones", command=abrir_obligaciones_window).grid(row=0, column=9, padx=5)
            
    # Botones
    btnGuardar = tk.Button(contenedor_formulario, text="Guardar", command=guardar_contrato)
    btnGuardar.pack(side='left', padx=5, pady=5)

    btnEliminar = tk.Button(contenedor_formulario, text="Eliminar", command=eliminar_contrato)
    btnEliminar.pack(side='left', padx=5, pady=5)

    btnLimpiar = tk.Button(contenedor_formulario, text="Limpiar", command=limpiar_campos)
    btnLimpiar.pack(side='left', padx=5, pady=5)

    # Campo de entrada para el filtro de `idVersion`
    tk.Label(contenedor_formulario, text="Filtro ID Versión:").pack(side='left', padx=5, pady=5)
    entry_filtro_id_version = tk.Entry(contenedor_formulario, textvariable=filtro_id_version)
    entry_filtro_id_version.pack(side='left', padx=5, pady=5)

    # Asociar la actualización automática al cambio de valor del filtro
    filtro_id_version.trace_add("write", lambda *args: llenar_tabla())

    # Scrollbar horizontal para la tabla
    scroll_horizontal = tk.Scrollbar(marco, orient='horizontal')
    scroll_horizontal.pack(side='bottom', fill='x')

    # Tabla (Treeview) con scroll horizontal
    tabla = ttk.Treeview(marco, columns=('ID', 'idVersion', 'Numero de documento', 'Cliente', 'Tipo Contrato', 'Cargo', 'Dependencia', 'Objeto', 'Descripción', 'Vigencia', 'Terminación', 'Autorización', 'Valor', 'obligaciones_especificas', 'consecutivo'), show='headings', xscrollcommand=scroll_horizontal.set)
    tabla.pack(fill='both', expand=True, padx=10, pady=10)

    # Configurar el scrollbar para que funcione con la tabla
    scroll_horizontal.config(command=tabla.xview)

    # Configurar las cabeceras de la tabla
    for col in tabla['columns']:
        tabla.heading(col, text=col)

    tabla.bind('<<TreeviewSelect>>', seleccionar_contrato)

    # Botones de Paginación
    contenedor_paginacion = tk.Frame(marco)
    contenedor_paginacion.pack(fill='x', padx=10, pady=5)

    btnAnterior = tk.Button(contenedor_paginacion, text="<< Anterior", command=ir_a_pagina_anterior)
    btnAnterior.pack(side='left', fill='x', expand=True)

    btnSiguiente = tk.Button(contenedor_paginacion, text="Siguiente >>", command=ir_a_pagina_siguiente)
    btnSiguiente.pack(side='right', fill='x', expand=True)

    # Campos de filtro
    contenedor_filtros = tk.Frame(marco)
    contenedor_filtros.pack(fill='x', padx=10, pady=5)

    tk.Label(contenedor_filtros, text="Filtro Cliente:").pack(side='left')
    comboFiltroCliente = ttk.Combobox(contenedor_filtros, textvariable=filtro_cliente)
    comboFiltroCliente.pack(side='left', fill='x', expand=True)
    filtro_cliente.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Tipo de Contrato:").pack(side='left')
    comboFiltroTipoContrato = ttk.Combobox(contenedor_filtros, textvariable=filtro_tipo_contrato)
    comboFiltroTipoContrato.pack(side='left', fill='x', expand=True)
    filtro_tipo_contrato.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Cargo:").pack(side='left')
    comboFiltroCargo = ttk.Combobox(contenedor_filtros, textvariable=filtro_cargo)
    comboFiltroCargo.pack(side='left', fill='x', expand=True)
    filtro_cargo.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Dependencia:").pack(side='left')
    comboFiltroDependencia = ttk.Combobox(contenedor_filtros, textvariable=filtro_dependencia)
    comboFiltroDependencia.pack(side='left', fill='x', expand=True)
    filtro_dependencia.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Autorización:").pack(side='left')
    tk.Entry(contenedor_filtros, textvariable=filtro_autorizacion).pack(side='left', fill='x', expand=True)
    filtro_autorizacion.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Valor:").pack(side='left')
    tk.Entry(contenedor_filtros, textvariable=filtro_valor).pack(side='left', fill='x', expand=True)
    filtro_valor.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Objeto:").pack(side='left')
    comboFiltroObjeto = ttk.Combobox(contenedor_filtros, textvariable=filtro_id_comboObjeto)
    comboFiltroObjeto.pack(side='left', fill='x', expand=True)
    filtro_id_comboObjeto.trace_add("write", lambda *args: llenar_tabla())

    tk.Label(contenedor_filtros, text="Filtro Obligaciones Específicas:").pack(side='left')
    comboFiltroObligaciones_Específicas  = ttk.Combobox(contenedor_filtros, textvariable=filtro_ObEspCon)
    comboFiltroObligaciones_Específicas.pack(side='left', fill='x', expand=True)
    filtro_id_Obligaciones.trace_add("write", lambda *args: llenar_tabla())

    # Botón de Mostrar Todos los Registros
    btnMostrarTodos = tk.Button(marco, text="Mostrar Todos los Registros", command=mostrar_todos_los_registros)
    btnMostrarTodos.pack(fill='x', padx=10, pady=5)

    # Función para calcular el término de ejecución
    def calcular_diferencia_fechas(fecha_inicio, fecha_fin):
        # Convertir las fechas de cadena a objetos datetime
        inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fin = datetime.strptime(fecha_fin, '%Y-%m-%d')

        # Calcular la diferencia en meses y días
        diferencia = relativedelta(fin, inicio)
        meses = diferencia.years * 12 + diferencia.months
        dias = diferencia.days

        # Si no ha pasado al menos un mes completo, dejar meses en 0
        if meses == 0 and dias > 0:
            meses = 0

        # Formatear en texto con números entre paréntesis
        resultado = f"{meses} Meses y {dias} días"
        return resultado

  # Función para convertir número a texto
    def convertir_valor_a_texto(valor):
        valor_texto = num2words(valor, lang='es').upper()  # Convertimos el número a palabras en español y en mayúsculas
        return f"{valor_texto} PESOS M/CTE."
    # Función para exportar a Word
    # Función para obtener la fecha actual en el formato requerido
    def obtener_fecha_actual_formateada():
        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Día en número
        dia = fecha_actual.day

        # Mes en texto
        mes = fecha_actual.strftime('%B').capitalize()

        # Año en número
        año = fecha_actual.year

        # Formato final: a los (día en número) días del mes de (mes en texto) del año (año en número)
        return f"a los {dia} días del mes de {mes} del año {año}"

    # Función para obtener el id, nombre completo y la ciudad de expedición del cliente
    def obtener_datos_cliente(cliente_id):
        try:
            # Consultar la información del cliente: id, nombres, apellidos y ciudad de expedición
            sql = """
            SELECT id, primerNombre, segundoNombre, primerApellido, segundoApellido, ciudadExpedicion
            FROM clientes
            WHERE id = %s
            """
            db.cursor.execute(sql, (cliente_id,))
            datos_cliente = db.cursor.fetchone()

            if datos_cliente:
                # Concatenamos los nombres y apellidos para formar el nombre completo
                nombre_completo = f"{datos_cliente[1]} {datos_cliente[2]} {datos_cliente[3]} {datos_cliente[4]}"
                ciudad_expedicion = datos_cliente[5]
                return datos_cliente[0], nombre_completo, ciudad_expedicion
            else:
                print(f"No se encontraron datos para el cliente con id {cliente_id}.")
                return None, None, None

        except Exception as e:
            print(f"Error al obtener datos del cliente: {e}")
            return None, None, None
    # Función para obtener el id del cliente basado en el nombre completo
    def obtener_id_cliente_por_nombre(nombre_completo):
        try:
            # Separar el nombre completo en las partes correspondientes
            partes_nombre = nombre_completo.split()
            primer_nombre = partes_nombre[0]
            segundo_nombre = partes_nombre[1] if len(partes_nombre) > 1 else ""
            primer_apellido = partes_nombre[2] if len(partes_nombre) > 2 else ""
            segundo_apellido = partes_nombre[3] if len(partes_nombre) > 3 else ""

            # Consulta SQL para obtener el id del cliente basado en su nombre completo
            sql = """
            SELECT id, ciudadExpedicion FROM clientes
            WHERE primerNombre = %s AND segundoNombre = %s AND primerApellido = %s AND segundoApellido = %s
            """
            print(f"Ejecutando consulta SQL para obtener ID: {sql} con nombre: {nombre_completo}")
            db.cursor.execute(sql, (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido))
            resultado = db.cursor.fetchone()

            if resultado:
                cliente_id = resultado[0]
                ciudad_expedicion = resultado[1]  # Obtenemos el id de la ciudadExpedicion
                print(f"ID del cliente obtenido: {cliente_id}, CiudadExpedicion ID: {ciudad_expedicion}")

                # Consulta SQL para obtener el nombre de la ciudad basado en el id de ciudadExpedicion
                sql_ciudad = """
                SELECT nombreCiudad FROM ciudad
                WHERE id = %s
                """
                db.cursor.execute(sql_ciudad, (ciudad_expedicion,))
                resultado_ciudad = db.cursor.fetchone()

                if resultado_ciudad:
                    nombreCiudad = resultado_ciudad[0]  # Obtenemos el nombre de la ciudad
                    print(f"Nombre de la ciudad obtenido: {nombreCiudad}")
                    return cliente_id, nombreCiudad
                else:
                    print(f"No se encontró la ciudad con id {ciudad_expedicion}")
                    return cliente_id, None
            else:
                print(f"No se encontró cliente con el nombre {nombre_completo}")
                return None, None

        except Exception as e:
            print(f"Error al obtener ID del cliente y la ciudad: {e}")
            return None, None
    # Función para obtener datos completos del cliente y contrato
    def obtener_datos_completos_cliente_y_contrato(cliente_id):
        try:
            sql = """
            SELECT 
                clientes.id, 
                CONCAT_WS(' ', clientes.primerNombre, clientes.segundoNombre, clientes.primerApellido, clientes.segundoApellido) AS nombreCompleto, 
                clientes.ciudadExpedicion, 
                contrato.ObEspCon, 
                contrato.autorizacionContratos,
                obligacionesespecificas.nombre AS nombreObligacion  -- Obtener el nombre de las obligaciones
            FROM 
                clientes
            JOIN 
                contrato ON clientes.id = contrato.idClientes
            LEFT JOIN 
                obligacionesespecificas ON contrato.ObEspCon = obligacionesespecificas.id  -- Unión para obtener el nombre
            WHERE 
                clientes.id = %s
            LIMIT 1
            """
            db.cursor.execute(sql, (cliente_id,))
            resultado = db.cursor.fetchone()
            if resultado:
                cliente_id, nombre_completo, ciudad_expedicion, obligaciones_especificas_id, autorizacion_contratos, nombre_obligacion = resultado
                return cliente_id, nombre_completo, ciudad_expedicion, nombre_obligacion, autorizacion_contratos  # Cambia para devolver el nombre
            else:
                return None, None, None, None, None
        except Exception as e:
            print(f"Error al obtener los datos del cliente y obligaciones: {e}")
            return None, None, None, None, None
    def nueva_version():
        try:
            # Obtener el valor actual del ID
            id_actual = id_independiente.get()

            if not id_actual:
                print("Error: No hay un ID seleccionado.")
                return

            # Consultar cuántos registros derivados existen para el ID actual
            sql = "SELECT COUNT(*) FROM contrato WHERE idVersion LIKE %s"
            db.cursor.execute(sql, (f"{id_actual}-%",))  # Usar el formato de idVersion derivado
            count_derivados = db.cursor.fetchone()[0]

            # Crear el valor para `idVersion` como `id-<número siguiente>`
            nuevo_id_version = f"{id_actual}-{count_derivados + 1}"

            # Obtener los datos del contrato actual
            sql_select = """
            SELECT idClientes, idTipoContrato, idCargo, idDependecia, idObjeto, 
            descripcionContrato, Vigencia, terminacion, autorizacionContratos, valorContrato, 
            ObEspCon, consecutivo FROM contrato WHERE id = %s
            """
            db.cursor.execute(sql_select, (id_actual,))
            contrato = db.cursor.fetchone()

            if contrato:
                # Desempaquetar los valores del contrato
                id_clientes, id_tipo_contrato, id_cargo, id_dependencia, id_idObjeto, descripcion, vigencia, terminacion, autorizacion, valor, obligaciones_especificas, consecutivo = contrato

                # Verificar la existencia de claves foráneas en las tablas relacionadas
                def verificar_existencia(tabla, campo, valor):
                    sql_verificar = f"SELECT id FROM {tabla} WHERE {campo} = %s"
                    db.cursor.execute(sql_verificar, (valor,))
                    return db.cursor.fetchone() is not None

                # Validar que todos los valores relacionados (claves foráneas) existan
                if (verificar_existencia("clientes", "id", id_clientes) and
                    verificar_existencia("tipodecontrato", "id", id_tipo_contrato) and
                    verificar_existencia("cargo", "id", id_cargo) and
                    verificar_existencia("dependencia", "id", id_dependencia) and
                    verificar_existencia("obligacionesespecificas", "id", obligaciones_especificas) and
                    verificar_existencia("objeto", "id", id_idObjeto)):

                    # Si todas las claves foráneas son válidas, insertar el nuevo registro
                    sql_insert = """
                    INSERT INTO contrato 
                    (idClientes, idTipoContrato, idCargo, idDependecia, idObjeto, descripcionContrato, 
                    Vigencia, terminacion, autorizacionContratos, valorContrato, ObEspCon, consecutivo, idVersion) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    valores = (
                        id_clientes, id_tipo_contrato, id_cargo, id_dependencia, id_idObjeto, descripcion,
                        vigencia, terminacion, autorizacion, valor, obligaciones_especificas,
                        consecutivo, nuevo_id_version
                    )
                    db.cursor.execute(sql_insert, valores)
                    db.cursor.connection.commit()

                    print(f"Nueva versión del contrato guardada con idVersion: {nuevo_id_version}")

                    # Actualizar la tabla en la interfaz
                    llenar_tabla()

                else:
                    print("Error: No se encontraron todas las claves foráneas requeridas en las tablas relacionadas.")

            else:
                print("Error: No se encontró el contrato con el ID proporcionado.")

        except Exception as e:
            print(f"Error al generar nueva versión del contrato: {e}")
            db.cursor.connection.rollback()

    # Función para exportar a Word
    def exportar_a_word():
        try:
            selected_item = tabla.selection()
            if selected_item:
                item = tabla.item(selected_item)
                contrato_seleccionado = item['values']
                objeto = contrato_seleccionado[7]
                obligaciones_especificas = comboObligaciones.get()  # Obtiene las obligaciones como un solo texto

                nombre_completo = contrato_seleccionado[3]
                consecutivo = contrato_seleccionado[14]
                print(f"Valor de consecutivo obtenido: {consecutivo}")

                cliente_id, nombreCiudad = obtener_id_cliente_por_nombre(nombre_completo)
                if cliente_id is None or nombreCiudad is None:
                    print(f"Error: No se pudo obtener el ID del cliente o la ciudad de expedición para {nombre_completo}.")
                    return

                plantilla_path = "Certificación Contractual No. 16X PLANTILLA DE CERTIFICACIONES.docx"
                doc = Document(plantilla_path)

                cliente_id, nombre_completo, ciudad_expedicion, nombre_obligacion, autorizacion_contratos = obtener_datos_completos_cliente_y_contrato(cliente_id)
                if cliente_id is None or nombre_completo is None or ciudad_expedicion is None or nombre_obligacion is None or autorizacion_contratos is None:
                    print("Error: No se pudo obtener la información del cliente.")
                    return

                vigencia_formateada = formatear_fecha_larga(datetime.strptime(str(contrato_seleccionado[9]), '%Y-%m-%d'))
                terminacion_formateada = formatear_fecha_larga(datetime.strptime(str(contrato_seleccionado[10]), '%Y-%m-%d'))
                termino_ejecutado = calcular_diferencia_fechas_texto(str(contrato_seleccionado[9]), str(contrato_seleccionado[10]))
                valor_contrato_texto = convertir_valor_a_texto(int(contrato_seleccionado[11]))
                fecha_actual_formateada = obtener_fecha_actual_formateada()

                for paragraph in doc.paragraphs:
                    if "XXXXXXXXXXXXX" in paragraph.text:
                        paragraph.text = paragraph.text.replace("XXXXXXXXXXXXX", nombre_completo)
                    if "XXXXXXX" in paragraph.text:
                        paragraph.text = paragraph.text.replace("XXXXXXX", str(cliente_id))
                    if "CO1.PCCNTR.5780050" in paragraph.text:
                        paragraph.text = paragraph.text.replace("CO1.PCCNTR.5780050", f"CO1.PCCNTR.{autorizacion_contratos}")
                    if "47.930.183" in paragraph.text:
                        paragraph.text = paragraph.text.replace("47.930.183", str(contrato_seleccionado[11]))
                    if "CUARENTA Y SIETE MILLONES NOVECIENTOS TREINTA MIL CIENTO OCHENTA Y TRES PESOS M/CTE." in paragraph.text:
                        paragraph.text = paragraph.text.replace("CUARENTA Y SIETE MILLONES NOVECIENTOS TREINTA MIL CIENTO OCHENTA Y TRES PESOS M/CTE.", valor_contrato_texto)
                    if "22 de enero de 2024" in paragraph.text:
                        paragraph.text = paragraph.text.replace("22 de enero de 2024", vigencia_formateada)
                    if "texto-objeto" in paragraph.text:
                        paragraph.text = paragraph.text.replace("texto-objeto", objeto)
                    if "13 de diciembre de 2024" in paragraph.text:
                        paragraph.text = paragraph.text.replace("13 de diciembre de 2024", terminacion_formateada)
                    if "Diez (10) Meses y Veintidós (22) días" in paragraph.text:
                        paragraph.text = paragraph.text.replace("Diez (10) Meses y Veintidós (22) días", termino_ejecutado)
                    if "a los 12 días del mes de julio del año 2024" in paragraph.text:
                        paragraph.text = paragraph.text.replace("a los 12 días del mes de julio del año 2024", fecha_actual_formateada)
                    if "valor Ciudad" in paragraph.text:
                        paragraph.text = paragraph.text.replace("valor Ciudad", nombreCiudad)

                    for paragraph in doc.paragraphs:
                        if "Obligaciones Específicas del Contrato: " in paragraph.text:
                            paragraph.clear()
                            run = paragraph.add_run("Obligaciones Específicas del Contrato: ")
                            run.bold = True
                            run.font.name = 'Calibri'
                            run.font.size = Pt(11)
                            run = paragraph.add_run(obligaciones_especificas.strip())
                            run.font.name = 'Calibri'
                            run.font.size = Pt(11)
                            paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                            paragraph.paragraph_format.space_before = Pt(10)
                            paragraph.paragraph_format.space_after = Pt(10)
                            paragraph.paragraph_format.line_spacing = Pt(16)

                for section in doc.sections:
                    header = section.header
                    for paragraph in header.paragraphs:
                        if "Certificación No. Consecutivo" in paragraph.text:
                            for run in paragraph.runs:
                                if "Consecutivo" in run.text:
                                    run.text = run.text.replace("Consecutivo", str(consecutivo))
                                    # Remover resaltado (resaltado amarillo)
                                    run.font.highlight_color = None
                            print(f"Encabezado actualizado con Consecutivo: {consecutivo}")
                doc_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
                if doc_path:
                    doc.save(doc_path)
                    print(f"Archivo Word guardado en: {doc_path}")
                    return doc_path  # Devolvemos la ruta para convertirla luego a PDF
                else:
                    print("Operación cancelada por el usuario.")
                    return None

        except Exception as e:
            print(f"Error al exportar a Word: {e}")
            return None
    # Función para calcular la diferencia en años, meses y días y formatearla en texto
    def calcular_diferencia_fechas_texto(fecha_inicio, fecha_fin):
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        diferencia = relativedelta(fecha_fin_dt, fecha_inicio_dt)
        anios = diferencia.years
        meses = diferencia.months
        dias = diferencia.days

        anios_texto = convertir_numero_a_texto(anios)
        meses_texto = convertir_numero_a_texto(meses)
        dias_texto = convertir_numero_a_texto(dias)

        # Formato con años, meses y días
        return f"{anios_texto.capitalize()} ({anios}) año(s), {meses_texto.capitalize()} ({meses}) meses y {dias_texto.capitalize()} ({dias}) días"

    # Función auxiliar para convertir números a texto
    def convertir_numero_a_texto(numero):
        numeros_texto = {
            0: 'Cero', 1: 'Uno', 2: 'Dos', 3: 'Tres', 4: 'Cuatro', 5: 'Cinco', 6: 'Seis', 7: 'Siete', 8: 'Ocho', 9: 'Nueve', 10: 'Diez',
            11: 'Once', 12: 'Doce', 13: 'Trece', 14: 'Catorce', 15: 'Quince', 16: 'Dieciséis', 17: 'Diecisiete', 18: 'Dieciocho', 19: 'Diecinueve', 20: 'Veinte',
            21: 'Veintiuno', 22: 'Veintidos', 23: 'Veintitres', 24: 'Veinticuatro', 25: 'Veinticinco', 26: 'Veintiseis', 27: 'Veintisiete', 28: 'Veintiocho', 29: 'Veintinueve', 30: 'Treinta', 31: 'Treinta y uno'
        }
        return numeros_texto.get(numero, str(numero))
    
    # Función para exportar a PDF
    def exportar_a_pdf():
        try:
            # Primero, exportamos el archivo a Word y obtenemos su ruta
            doc_path = exportar_a_word()
            if doc_path:
                # Luego, convertimos ese archivo de Word a PDF
                pdf_path = doc_path.replace(".pdf")
                convert(pdf_path)
                print(f"Archivo PDF guardado en: {pdf_path}")
            else:
                print("No se pudo generar el PDF ya que el archivo Word no fue exportado correctamente.")
        
        except Exception as e:
            print(f"Error al exportar a PDF: {e}")
    # Función para calcular la diferencia en años, meses y días y formatearla en texto
    def calcular_diferencia_fechas_texto(fecha_inicio, fecha_fin):
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        diferencia = relativedelta(fecha_fin_dt, fecha_inicio_dt)
        anios = diferencia.years
        meses = diferencia.months
        dias = diferencia.days

        anios_texto = convertir_numero_a_texto(anios)
        meses_texto = convertir_numero_a_texto(meses)
        dias_texto = convertir_numero_a_texto(dias)

        # Formato con años, meses y días
        return f"{anios_texto.capitalize()} ({anios}) año(s), {meses_texto.capitalize()} ({meses}) Meses y {dias_texto.capitalize()} ({dias}) días"

    # Función auxiliar para convertir números a texto
    def convertir_numero_a_texto(numero):
        numeros_texto = {
            0: 'Cero', 1: 'Uno', 2: 'Dos', 3: 'Tres', 4: 'Cuatro', 5: 'Cinco', 6: 'Seis', 7: 'Siete', 8: 'Ocho', 9: 'Nueve', 10: 'Diez',
            11: 'Once', 12: 'Doce', 13: 'Trece', 14: 'Catorce', 15: 'Quince', 16: 'Dieciséis', 17: 'Diecisiete', 18: 'Dieciocho', 19: 'Diecinueve', 20: 'Veinte',
            21: 'Veintiuno', 22: 'Veintidós', 23: 'Veintitrés', 24: 'Veinticuatro', 25: 'Veinticinco', 26: 'Veintiséis', 27: 'Veintisiete', 28: 'Veintiocho', 29: 'Veintinueve', 30: 'Treinta', 31: 'Treinta y uno'
        }
        return numeros_texto.get(numero, str(numero))

    def exportar_a_excel():
        try:
            # Abrir un diálogo para que el usuario seleccione la ubicación y nombre del archivo
            archivo_excel = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Archivos de Excel", "*.xlsx")],
                title="Guardar archivo de Excel"
            )
            
            if archivo_excel:  # Si el usuario selecciona una ubicación
                # Conectar a la base de datos
                conexion = pymysql.connect(host='localhost', user='root', password='', db='contrataciones')
                cursor = conexion.cursor()

                # Consulta SQL para obtener los datos con nombres en lugar de IDs y agregar idVersion e idClientes
                consulta = """
                SELECT
                    contrato.id,
                    contrato.idVersion,
                    contrato.idClientes,
                    contrato.descripcionContrato,
                    contrato.Vigencia,
                    contrato.terminacion,
                    contrato.autorizacionContratos,
                    contrato.valorContrato,
                    contrato.consecutivo,

                    CONCAT(clientes.primerNombre, ' ', clientes.segundoNombre, ' ', clientes.primerApellido, ' ', clientes.segundoApellido) AS nombreCliente,

                    tipodecontrato.nombreTipoContrato,

                    cargo.nombreCargo,

                    dependencia.nombreDependencia,

                    objeto.nombreObjeto,

                    obligacionesespecificas.nombre AS nombreObligacionEspecifica

                FROM contrato
                LEFT JOIN clientes ON contrato.idClientes = clientes.id
                LEFT JOIN tipodecontrato ON contrato.idTipoContrato = tipodecontrato.id
                LEFT JOIN cargo ON contrato.idCargo = cargo.id
                LEFT JOIN dependencia ON contrato.idDependecia = dependencia.id
                LEFT JOIN objeto ON contrato.idObjeto = objeto.id
                LEFT JOIN obligacionesespecificas ON contrato.ObEspCon = obligacionesespecificas.id
                """

                # Ejecutar la consulta
                cursor.execute(consulta)
                registros = cursor.fetchall()

                # Crear un DataFrame de pandas con los resultados
                columnas = [
                    'ID Contrato', 'ID Versión', 'ID Cliente', 'Descripción Contrato', 'Vigencia', 'Terminación', 
                    'Autorización', 'Valor Contrato', 'Consecutivo', 'Nombre Cliente', 
                    'Tipo de Contrato', 'Cargo', 'Dependencia', 'Objeto', 'Obligación Específica'
                ]
                df = pd.DataFrame(registros, columns=columnas)

                # Asegurar que las fechas se formateen adecuadamente
                df['Vigencia'] = pd.to_datetime(df['Vigencia']).dt.strftime('%Y-%m-%d')
                df['Terminación'] = pd.to_datetime(df['Terminación']).dt.strftime('%Y-%m-%d')

                # Exportar el DataFrame a un archivo Excel en la ruta seleccionada
                df.to_excel(archivo_excel, index=False)

                # Ajustar el ancho de todas las columnas, incluida "Obligación Específica"
                ajustar_ancho_columnas(archivo_excel)

                print(f"Registros exportados a {archivo_excel} exitosamente.")
                messagebox.showinfo("Exportación exitosa", f"Registros exportados a {archivo_excel}")

        except Exception as e:
            print(f"Error al exportar a Excel: {e}")
            messagebox.showerror("Error", f"Error al exportar a Excel: {e}")

        finally:
            conexion.close()


    def ajustar_ancho_columnas(archivo_excel):
        # Cargar el archivo Excel recién creado
        libro = load_workbook(archivo_excel)
        hoja = libro.active

        # Iterar sobre las columnas y ajustar el ancho basado en el contenido
        for col in hoja.columns:
            max_length = 0
            col_letter = get_column_letter(col[0].column)  # Obtener la letra de la columna

            for cell in col:
                try:
                    # Obtener la longitud máxima de los valores en la columna
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except:
                    pass

            # Ajustar el ancho de la columna (agregar un pequeño margen)
            hoja.column_dimensions[col_letter].width = max_length + 2

        # Guardar el archivo con los cambios
        libro.save(archivo_excel)

    def importar_desde_excel():
        try:
            # Abrir un diálogo para que el usuario seleccione el archivo Excel
            archivo_excel = filedialog.askopenfilename(
                filetypes=[("Archivos de Excel", "*.xlsx")],
                title="Seleccionar archivo de Excel"
            )
            
            if archivo_excel:  # Si el usuario selecciona un archivo
                # Leer el archivo Excel
                df = pd.read_excel(archivo_excel)

                # Conectar a la base de datos
                conexion = pymysql.connect(host='localhost', user='root', password='', db='contrataciones')
                cursor = conexion.cursor()

                # Recorrer el DataFrame y preparar la inserción de datos
                for index, row in df.iterrows():
                    # Obtener el ID del tipo de contrato a partir del nombre
                    cursor.execute("SELECT id FROM tipodecontrato WHERE nombreTipoContrato = %s", (row['Tipo de Contrato'],))
                    id_tipo_contrato = cursor.fetchone()[0]

                    # Obtener el ID del cargo a partir del nombre
                    cursor.execute("SELECT id FROM cargo WHERE nombreCargo = %s", (row['Cargo'],))
                    id_cargo = cursor.fetchone()[0]

                    # Obtener el ID de la dependencia a partir del nombre
                    cursor.execute("SELECT id FROM dependencia WHERE nombreDependencia = %s", (row['Dependencia'],))
                    id_dependencia = cursor.fetchone()[0]

                    # Obtener el ID del objeto a partir del nombre
                    cursor.execute("SELECT id FROM objeto WHERE nombreObjeto = %s", (row['Objeto'],))
                    id_objeto = cursor.fetchone()[0]

                    # Obtener el ID de la obligación específica a partir del nombre
                    cursor.execute("SELECT id FROM obligacionesespecificas WHERE nombre = %s", (row['Obligación Específica'],))
                    id_obligacion = cursor.fetchone()[0]

                    # Preparar la inserción de datos, excluyendo "Nombre Cliente"
                    insertar_contrato = """
                    INSERT INTO contrato (idVersion, idClientes, descripcionContrato, Vigencia, terminacion, autorizacionContratos, valorContrato, consecutivo, 
                                        idTipoContrato, idCargo, idDependecia, idObjeto, ObEspCon)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    datos = (
                        row['ID Versión'],
                        row['ID Cliente'],  # Este se mantiene
                        row['Descripción Contrato'],
                        row['Vigencia'],
                        row['Terminación'],
                        row['Autorización'],
                        row['Valor Contrato'],
                        row['Consecutivo'],
                        id_tipo_contrato,  # Guardamos el ID del tipo de contrato
                        id_cargo,  # Guardamos el ID del cargo
                        id_dependencia,  # Guardamos el ID de la dependencia
                        id_objeto,  # Guardamos el ID del objeto
                        id_obligacion  # Guardamos el ID de la obligación específica
                    )

                    # Ejecutar la inserción en la tabla de contratos
                    cursor.execute(insertar_contrato, datos)

                # Confirmar los cambios
                conexion.commit()

                print("Datos importados exitosamente.")
                messagebox.showinfo("Importación exitosa", "Datos importados exitosamente desde el archivo Excel.")

        except Exception as e:
            print(f"Error al importar desde Excel: {e}")
            messagebox.showerror("Error", f"Error al importar desde Excel: {e}")

        finally:
            conexion.close()
    # Colocando cada botón en una columna diferente de la misma fila
    btnExportarWord = tk.Button(marco_botones, text="Exportar a Word", command=exportar_a_word)
    btnExportarWord.grid(row=0, column=0, padx=5, pady=5, sticky="ew")  # Primera columna

    btnExportarPDF = tk.Button(marco_botones, text="Exportar a PDF", command=exportar_a_pdf)
    btnExportarPDF.grid(row=0, column=1, padx=5, pady=5, sticky="ew")  # Segunda columna

    btnNuevaVersion = tk.Button(marco_botones, text="Nueva Versión", command=nueva_version)
    btnNuevaVersion.grid(row=0, column=2, padx=5, pady=5, sticky="ew")  # Tercera columna

    btnExportarExcel = tk.Button(marco_botones, text="Exportar a Excel", command=exportar_a_excel)
    btnExportarExcel.grid(row=0, column=3, padx=5, pady=5, sticky="ew")  # Cuarta columna

    btnImportarExcel = tk.Button(marco_botones, text="Importar desde Excel", command=importar_desde_excel)
    btnImportarExcel.grid(row=0, column=4, padx=5, pady=5, sticky="ew")  # Quinta columna

    # Expande cada botón para ocupar el ancho de su columna
    for i in range(5):
        marco_botones.grid_columnconfigure(i, weight=1)
    # Cargar datos en la tabla
    llenar_tabla()
    cargar_combo_data()
    actualizar_botones_paginacion()

def mostrar_Contratista(frame):
    pass

def mostrar_jefes(frame):
    pass

def mostrar_usuario(frame):
    global db, page_number, records_per_page, total_records
    db = DataBase()
    modificar = False
    
    # Variables
    numero_cedula_cliente = ctk.StringVar()
    correo_cli = ctk.StringVar()
    contrasena_cli = ctk.StringVar()
    filtro_cedula = ctk.StringVar()
    filtro_correo = ctk.StringVar()
    
    # Variables de paginación
    page_number = 1
    records_per_page = 10
    total_records = 0

    def solo_numeros(event):
        contenido = numero_cedula_cliente.get()
        if not contenido.isdigit():
            numero_cedula_cliente.set(''.join(filter(str.isdigit, contenido)))

    def limpiar():
        numero_cedula_cliente.set("")
        correo_cli.set("")
        contrasena_cli.set("")
        filtro_cedula.set("")
        filtro_correo.set("")

    def llenar_tabla():
        global total_records
        offset = (page_number - 1) * records_per_page
        
        try:
            sql_count = "SELECT COUNT(*) FROM usuarios WHERE 1=1"
            sql = "SELECT id, numeroCedulaCliente, correoCli, contraseñaCli FROM usuarios WHERE 1=1"
            parametros = []
            
            if filtro_cedula.get():
                sql_count += " AND numeroCedulaCliente LIKE %s"
                sql += " AND numeroCedulaCliente LIKE %s"
                parametros.append(f"%{filtro_cedula.get()}%")

            if filtro_correo.get():
                sql_count += " AND correoCli LIKE %s"
                sql += " AND correoCli LIKE %s"
                parametros.append(f"%{filtro_correo.get()}%")

            db.cursor.execute(sql_count, tuple(parametros))
            total_records = db.cursor.fetchone()[0]

            sql += " LIMIT %s OFFSET %s"
            parametros.extend([records_per_page, offset])
            db.cursor.execute(sql, tuple(parametros))
            usuarios = db.cursor.fetchall()

            for usuario in usuarios:
                tabla.insert("", 'end', iid=usuario[0], values=usuario)

        except Exception as e:
            lblMensaje.configure(text=f"Error al llenar la tabla: {e}", fg_color="red")

    def seleccionar(event):
        seleccion = tabla.selection()
        if seleccion:
            id = seleccion[0]
            valores = tabla.item(id, "values")
            numero_cedula_cliente.set(valores[1])
            correo_cli.set(valores[2])
            contrasena_cli.set(valores[3])
    
    def nuevo():
        if not numero_cedula_cliente.get() or not correo_cli.get() or not contrasena_cli.get():
            lblMensaje.configure(text="Todos los campos son obligatorios", fg_color="red")
            return
        
        try:
            hashed_password = bcrypt.hashpw(contrasena_cli.get().encode('utf-8'), bcrypt.gensalt())
            sql = "INSERT INTO usuarios (numeroCedulaCliente, correoCli, contraseñaCli) VALUES (%s, %s, %s)"
            db.cursor.execute(sql, (numero_cedula_cliente.get(), correo_cli.get(), hashed_password))
            db.connection.commit()
            lblMensaje.configure(text="Registro guardado", fg_color="green")
            llenar_tabla()
            limpiar()
        except Exception as e:
            lblMensaje.configure(text=f"Error al guardar: {e}", fg_color="red")
    
    def actualizar():
        seleccion = tabla.selection()
        if seleccion:
            id = seleccion[0]
            try:
                hashed_password = bcrypt.hashpw(contrasena_cli.get().encode('utf-8'), bcrypt.gensalt())
                sql = "UPDATE usuarios SET numeroCedulaCliente=%s, correoCli=%s, contraseñaCli=%s WHERE id=%s"
                db.cursor.execute(sql, (numero_cedula_cliente.get(), correo_cli.get(), hashed_password, id))
                db.connection.commit()
                lblMensaje.configure(text="Registro actualizado", fg_color="green")
                llenar_tabla()
                limpiar()
            except Exception as e:
                lblMensaje.configure(text=f"Error al actualizar: {e}", fg_color="red")
        else:
            lblMensaje.configure(text="Seleccione un registro", fg_color="red")
    
    def eliminar():
        seleccion = tabla.selection()
        if seleccion:
            id = seleccion[0]
            try:
                sql = "DELETE FROM usuarios WHERE id=%s"
                db.cursor.execute(sql, (id,))
                db.connection.commit()
                tabla.delete(id)
                lblMensaje.configure(text="Registro eliminado", fg_color="green")
                llenar_tabla()
            except Exception as e:
                lblMensaje.configure(text=f"Error al eliminar: {e}", fg_color="red")
        else:
            lblMensaje.configure(text="Seleccione un registro", fg_color="red")

    # Interfaz gráfica
    marco_usuario = ctk.CTkFrame(frame, fg_color="transparent")
    marco_usuario.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Campos de entrada
    ctk.CTkLabel(marco_usuario, text="Cédula Cliente").grid(row=0, column=0)
    txtCedula = ctk.CTkEntry(marco_usuario, textvariable=numero_cedula_cliente)
    txtCedula.grid(row=0, column=1)
    txtCedula.bind("<KeyRelease>", solo_numeros)
    
    ctk.CTkLabel(marco_usuario, text="Correo").grid(row=1, column=0)
    ctk.CTkEntry(marco_usuario, textvariable=correo_cli).grid(row=1, column=1)
    
    ctk.CTkLabel(marco_usuario, text="Contraseña").grid(row=2, column=0)
    ctk.CTkEntry(marco_usuario, textvariable=contrasena_cli, show="*").grid(row=2, column=1)
    
    lblMensaje = ctk.CTkLabel(marco_usuario, text="", fg_color="transparent")
    lblMensaje.grid(row=3, column=0, columnspan=2)
    
    # Botones
    ctk.CTkButton(marco_usuario, text="Nuevo", command=nuevo).grid(row=4, column=0)
    ctk.CTkButton(marco_usuario, text="Actualizar", command=actualizar).grid(row=4, column=1)
    ctk.CTkButton(marco_usuario, text="Eliminar", command=eliminar).grid(row=5, column=0, columnspan=2)
    
    # Tabla de usuarios
    columnas = ("ID", "Cédula", "Correo", "Contraseña")
    tabla = ttk.Treeview(marco_usuario, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
    tabla.grid(row=6, column=0, columnspan=2)
    tabla.bind("<<TreeviewSelect>>", seleccionar)
    
    llenar_tabla()


############################################## Pantalla Bienvenida ###################################################
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
        "Pantalla Tipo de contrato", "Pantalla Dependencia", "Pantalla Departamento", 
        "Pantalla Tipo de Cuenta", "Pantalla Contrato",
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