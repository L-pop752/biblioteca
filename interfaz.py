import mysql.connector
import tkinter as tk
from tkinter import messagebox
from conexion import conectar

conn = conectar()

ventana = tk.Tk()
ventana.title("Sistema de Biblioteca")
ventana.geometry("350x450")
ventana.grid_columnconfigure(0, weight=1)

todos_los_frames = []

def mostrar_frame(frame_a_mostrar):
    for f in todos_los_frames:
        f.grid_forget()
    frame_a_mostrar.grid(row=1, column=0, sticky="nsew", padx=20)


def ir_a_agregar():
    mostrar_frame(frame_agregar)

def ir_a_editar():
    mostrar_frame(frame_editar)

def ir_a_consultar():
    mostrar_frame(frame_consultar)

def ir_a_eliminar():
    mostrar_frame(frame_eliminar)


def volver_al_menu():
    mostrar_frame(frame_menu)


lbl_principal = tk.Label(ventana, text="Biblioteca", font=("Arial", 20, "bold"))
lbl_principal.grid(row=0, column=0, pady=20)


frame_menu = tk.Frame(ventana)
frame_menu.grid_columnconfigure(0, weight=1)
todos_los_frames.append(frame_menu)

btn_agregar = tk.Button(frame_menu, text="Agregar Libro", font=("Arial", 14), width=18, bg="#d4edda", command=ir_a_agregar)
btn_agregar.grid(row=0, column=0, pady=10)

btn_editar = tk.Button(frame_menu, text="Editar Libro", font=("Arial", 14), width=18, bg="#fff3cd", command=ir_a_editar)
btn_editar.grid(row=1, column=0, pady=10)

btn_consultar = tk.Button(frame_menu, text="Consultar Libro", font=("Arial", 14), width=18, bg="#d1ecf1", command=ir_a_consultar)
btn_consultar.grid(row=2, column=0, pady=10)

btn_eliminar = tk.Button(frame_menu, text="Eliminar Libro", font=("Arial", 14), width=18, bg="#f8d7da", command=ir_a_eliminar)
btn_eliminar.grid(row=3, column=0, pady=10)


frame_agregar = tk.Frame(ventana)
frame_agregar.grid_columnconfigure(0, weight=1)
frame_agregar.grid_columnconfigure(1, weight=1)
todos_los_frames.append(frame_agregar)

lbl_form_agregar = tk.Label(frame_agregar, text="Registrar Nuevo Libro", font=("Arial", 14, "bold"))
lbl_form_agregar.grid(row=0, column=0, columnspan=2, pady=15)

lbl_titulo_agregar = tk.Label(frame_agregar, text="Título:")
lbl_titulo_agregar.grid(row=1, column=0, padx=5, pady=10, sticky="e")
entry_titulo_agregar = tk.Entry(frame_agregar, width=20)
entry_titulo_agregar.grid(row=1, column=1, padx=5, pady=10)

lbl_autor_agregar = tk.Label(frame_agregar, text="Autor:")
lbl_autor_agregar.grid(row=2, column=0, padx=5, pady=10, sticky="e")
entry_autor_agregar = tk.Entry(frame_agregar, width=20)
entry_autor_agregar.grid(row=2, column=1, padx=5, pady=10)


def guardar():
    titulo = entry_titulo_agregar.get().strip()
    autor = entry_autor_agregar.get().strip()

    if not titulo or not autor:
        messagebox.showwarning("Campos obligatorios", "El título y el autor no pueden estar vacíos")
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO libros (titulo, autor) VALUES (%s, %s)",
            (titulo, autor)
        )
        conn.commit()
        messagebox.showinfo("Éxito", "Libro agregado correctamente")
        entry_titulo_agregar.delete(0, tk.END)
        entry_autor_agregar.delete(0, tk.END)
        volver_al_menu()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Ese libro ya existe")


btn_guardar = tk.Button(frame_agregar, text="Guardar", bg="lightgreen", font=("Arial", 11), width=10, command=guardar)
btn_guardar.grid(row=3, column=0, columnspan=2, pady=10)

btn_volver_agregar = tk.Button(frame_agregar, text="Volver", bg="lightgray", font=("Arial", 11), width=10, command=volver_al_menu)
btn_volver_agregar.grid(row=4, column=0, columnspan=2, pady=5)


frame_editar = tk.Frame(ventana)
frame_editar.grid_columnconfigure(0, weight=1)
frame_editar.grid_columnconfigure(1, weight=1)
todos_los_frames.append(frame_editar)

lbl_form_editar = tk.Label(frame_editar, text="Editar Libro", font=("Arial", 14, "bold"))
lbl_form_editar.grid(row=0, column=0, columnspan=2, pady=15)

lbl_id_editar = tk.Label(frame_editar, text="ID del libro:")
lbl_id_editar.grid(row=1, column=0, padx=5, pady=10, sticky="e")
entry_id_editar = tk.Entry(frame_editar, width=20)
entry_id_editar.grid(row=1, column=1, padx=5, pady=10)

lbl_titulo_editar = tk.Label(frame_editar, text="Nuevo título:")
lbl_titulo_editar.grid(row=2, column=0, padx=5, pady=10, sticky="e")
entry_titulo_editar = tk.Entry(frame_editar, width=20)
entry_titulo_editar.grid(row=2, column=1, padx=5, pady=10)

lbl_autor_editar = tk.Label(frame_editar, text="Nuevo autor:")
lbl_autor_editar.grid(row=3, column=0, padx=5, pady=10, sticky="e")
entry_autor_editar = tk.Entry(frame_editar, width=20)
entry_autor_editar.grid(row=3, column=1, padx=5, pady=10)

def guardar_edicion():
    id_libro = entry_id_editar.get().strip()
    titulo = entry_titulo_editar.get().strip()
    autor = entry_autor_editar.get().strip()

    if not id_libro:
        messagebox.showwarning("Falta el ID", "Escribe el ID del libro que quieres editar")
        return

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE libros SET titulo = %s, autor = %s WHERE id = %s",
        (titulo, autor, id_libro)
    )
    conn.commit()
    messagebox.showinfo("Actualizado", "Libro actualizado correctamente")
    volver_al_menu()


btn_guardar_editar = tk.Button(frame_editar, text="Guardar cambios", bg="lightgreen", font=("Arial", 11), width=14, command=guardar_edicion)
btn_guardar_editar.grid(row=4, column=0, columnspan=2, pady=10)

btn_volver_editar = tk.Button(frame_editar, text="Volver", bg="lightgray", font=("Arial", 11), width=10, command=volver_al_menu)
btn_volver_editar.grid(row=5, column=0, columnspan=2, pady=5)

frame_consultar = tk.Frame(ventana)
frame_consultar.grid_columnconfigure(0, weight=1)
frame_consultar.grid_columnconfigure(1, weight=1)
todos_los_frames.append(frame_consultar)

lbl_form_consultar = tk.Label(frame_consultar, text="Consultar Libro", font=("Arial", 14, "bold"))
lbl_form_consultar.grid(row=0, column=0, columnspan=2, pady=15)

lbl_buscar = tk.Label(frame_consultar, text="Título o autor:")
lbl_buscar.grid(row=1, column=0, padx=5, pady=10, sticky="e")
entry_buscar = tk.Entry(frame_consultar, width=20)
entry_buscar.grid(row=1, column=1, padx=5, pady=10)

lbl_resultado = tk.Label(frame_consultar, text="", justify="left", wraplength=280)
lbl_resultado.grid(row=2, column=0, columnspan=2, pady=10)

def buscar():
    texto = entry_buscar.get().strip()
    if not texto:
        return

    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, titulo, autor FROM libros WHERE titulo LIKE %s OR autor LIKE %s",
        (f"%{texto}%", f"%{texto}%")
    )
    resultados = cursor.fetchall()

    if not resultados:
        lbl_resultado.config(text="No se encontraron libros.")
        return

    texto_resultado = ""
    for id_libro, titulo, autor in resultados:
        texto_resultado += f"ID {id_libro}: {titulo} - {autor}\n"
    lbl_resultado.config(text=texto_resultado)


btn_buscar = tk.Button(frame_consultar, text="Buscar", bg="lightblue", font=("Arial", 11), width=10, command=buscar)
btn_buscar.grid(row=3, column=0, columnspan=2, pady=10)

btn_volver_consultar = tk.Button(frame_consultar, text="Volver", bg="lightgray", font=("Arial", 11), width=10, command=volver_al_menu)
btn_volver_consultar.grid(row=4, column=0, columnspan=2, pady=5)

frame_eliminar = tk.Frame(ventana)
frame_eliminar.grid_columnconfigure(0, weight=1)
frame_eliminar.grid_columnconfigure(1, weight=1)
todos_los_frames.append(frame_eliminar)

lbl_form_eliminar = tk.Label(frame_eliminar, text="Eliminar Libro", font=("Arial", 14, "bold"))
lbl_form_eliminar.grid(row=0, column=0, columnspan=2, pady=15)

lbl_id_eliminar = tk.Label(frame_eliminar, text="ID del libro:")
lbl_id_eliminar.grid(row=1, column=0, padx=5, pady=10, sticky="e")
entry_id_eliminar = tk.Entry(frame_eliminar, width=20)
entry_id_eliminar.grid(row=1, column=1, padx=5, pady=10)

def eliminar():
    id_libro = entry_id_eliminar.get().strip()
    if not id_libro:
        messagebox.showwarning("Falta el ID", "Escribe el ID del libro que quieres eliminar")
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar el libro con ID {id_libro}?")
    if confirmar:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM libros WHERE id = %s", (id_libro,))
        conn.commit()
        messagebox.showinfo("Eliminado", "Libro eliminado correctamente")
        entry_id_eliminar.delete(0, tk.END)
        volver_al_menu()


btn_eliminar_confirmar = tk.Button(frame_eliminar, text="Eliminar", bg="#f8d7da", font=("Arial", 11), width=10, command=eliminar)
btn_eliminar_confirmar.grid(row=2, column=0, columnspan=2, pady=10)

btn_volver_eliminar = tk.Button(frame_eliminar, text="Volver", bg="lightgray", font=("Arial", 11), width=10, command=volver_al_menu)
btn_volver_eliminar.grid(row=3, column=0, columnspan=2, pady=5)

mostrar_frame(frame_menu)

ventana.mainloop()