preguntas_cuestionario = [
    '¿Has tenido algún tratamiento previo en Salud Mental?\n (a)Sí\n (b)No\n\n',
    '¿Has tenido alguno de los siguientes diagnósticos?\n (a)Trastorno de la Conducta Alimentaria (Anorexia-Bulimia)\n (b)Trastorno Depresivo Severo\n (c)Trastorno Obsesivo-Compulsivo\n (d)Trastorno Psicótico\n (e)Trastorno de la Personalidad\n (f)Ninguna de las anteriores\n\n',
    'De las siguientes afirmaciones, cual responde mejor a lo que tú esperas de una atención en salud mental\n (a)Abordar algo ocurrido recientemente(último mes)\n (b)Retomar tratamiento psicológico\n (c)Retomar tratamiento psiquiátrico\n\n',
    '¿Qué esperas de tu solicitud de ayuda en salud mental?\n (a)Resolver un problema o necesidad específica de algo ocurrido recientemente\n (b)Abordar un problema o necesidad en el que me puedan brindar herramientas concretas en un periodo acotado de tiempo\n (c)Poder acompañar un proceso reflexivo sobre problemas o necesidades específicas que llevo desde hace un tiempo\n\n',
    'Tu problema o necesidad específica se ajusta a alguno de los siguientes tópicos\n (a)Problemas de ansiedad, estrés y sueño\n (b)Problemas con mi estado anímico\n (c)Problemas en mis relaciones interpersonales (pareja, amigos, familia)\n (d)Problemas con el consumo de alcohol, cigarro u otras drogas\n (e)Ninguna de las anteriores\n'
]

consejerias = [
    'Prevención de la Depresión'
    'Prevención de Ansiedad, Estrés y Sueño'
    'Autocuidado en Consumo de Drogas'
    'Apoyo a la Diversidad'
    'Relaciones saludables'
]

respuestas_cuestionario = [
    'En consideración a tus respuestas te sugerimos agendar una hora del Servicio de Orientación Inmediata (SOI)'
    f'En consideración a tus respuestas te sugerimos agendar una hora del Servicio de Consejería en {consejerias}'
    'En consideración a tus respuestas te sugerimos agendar una hora del Servicio de Psicoterapia Focal'
    'En consideración a tus respuestas te sugerimos agendar una hora del Servicio de Derivación Asistida'
]

class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

listadopreguntas = [
    Pregunta(preguntas_cuestionario[0], None),
    Pregunta(preguntas_cuestionario[1], None),
    Pregunta(preguntas_cuestionario[2], None),
    Pregunta(preguntas_cuestionario[3], None),
    Pregunta(preguntas_cuestionario[4], None)
    ]

#este bloque de codigo es el que debo ajustar con if, else etc. para ajustar las ramificaciones de las preguntas#
def run_test(listadopreguntas):
    omitir_pregunta = False
    for x in listadopreguntas:
        answer = input(x.pregunta) #las dos lineas anteriores permiten que el ciclo for genere el paso por todas las preguntas de la variable "listadopreguntas"#
        if answer == "b":
            omitir_pregunta = True
        elif answer != "a":
            break


run_test(listadopreguntas)



#antes de crear el objeto de pregunta, hay que importar la clase de pregunta, no obstante acá la clase ya está definida en el mismo paquete de codigo#

#preguntas = [
#    Pregunta(preguntas_cuestionario[0],"a" or "b") #el problema acá es que necesito que cada pregunta considere como validas cualquiera de las dos respuestas, creo que el "or" no es una herramienta valida#