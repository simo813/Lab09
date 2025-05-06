import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.controls = []
        self._view.update_page()
        distanza = self._view.txt_distanza.value
        if distanza is None or distanza == "" or self.is_integer(distanza) != True:
            self._view.create_alert("Inserire il valore correttamente")
            return
        graph = self._model.buildGraph(distanza)
        nVertici = graph.number_of_nodes()
        nArchi = graph.number_of_edges()
        listaArchi = list(graph.edges(data=True))
        self._view.txt_result.controls.append(ft.Text(f"Il numero di nodi è: {nVertici}\n"
                                                      f"Il numero di archi è: {nArchi}\n"
                                                      f"{self.strArchi(listaArchi)}"))
        self._view.update_page()

    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def strArchi(self, listaArchi):
        stampa = "Lista archi:\n"
        for arco in listaArchi:
            stampa += f"Aeroporto di partenza: {arco[0]} Aeroporto di arrivo: {arco[1]} Distanza: {arco[2]['weight']}\n"

        return stampa



