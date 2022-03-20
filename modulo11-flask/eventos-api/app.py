import json
from flask import Flask, jsonify
from evento import Evento
from evento_online import EventoOnline

app = Flask(__name__)

ev1 = Evento("Aula de Python")
ev1.imprime_informacaoes()
ev2 = Evento("Aula de Javascript", "Florianópolis")
ev2.imprime_informacaoes()

ev1_online = EventoOnline("Live de Python")
ev1_online.imprime_informacaoes()

ev2_online = EventoOnline("Live de Javascript")
ev2_online.imprime_informacaoes()

eventos = [ev1, ev2, ev1_online, ev2_online]

find = lambda func, elements: next((element for element in elements if func(element)), None)
findall = lambda func, elements: [element for element in elements if func(element)]


@app.route("/")
def index():
    return "<h1>Flask successfully installed! 😎</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []

    for ev in eventos:
        eventos_dict.append(ev.__dict__)

    return jsonify(eventos_dict)
    
# @app.route("/api/eventos/<int:id>/")
# def detalhar_evento(id):
#     for ev in eventos:
#         if ev.id == id:
#             return jsonify(ev.__dict__)

@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    evento = find(lambda ev: ev.id == id, eventos)

    return jsonify(evento.__dict__)