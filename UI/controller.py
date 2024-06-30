import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        citta = self._view.dd_citta.value
        if citta is None:
            self._view.create_alert("Selezionare una citta")
            return
        anno = self._view.dd_anno.value
        if anno is None:
            self._view.create_alert("Selezionare un Anno")
            return
        grafo = self._model.creaGrafo(citta, int(anno))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for locale in grafo.nodes:
            self._view.dd_locale.options.append(ft.dropdown.Option(
                text=locale))
        self._view.update_page()

    def handle_migliore(self, e):
        migliore=self._model.migliore()
        self._view.txt_result.controls.append(ft.Text(f"LOCALE MIGLIORE {migliore}"))
        self._view.update_page()


    def handle_percorso(self, e):
        miglioramento = self._view.txt_soglia.value
        if miglioramento == "":
            self._view.create_alert("Inserire una soglia di miglioramento")
            return
        if float(miglioramento) >1 or float(miglioramento) <0:
            self._view.create_alert("Inserire un numero tra 0 e 1 ")
            return
        locale = self._view.dd_locale.value
        if locale is None:
            self._view.create_alert("Selezionare un locale")
            return
        costo, listaNodi = self._model.getBestPath( float(miglioramento),locale)
        self._view.txt_result.controls.append(ft.Text(f"La soluzione migliore è costituita da {costo} locali"))
        for i in range (0, len(listaNodi)-1):
            self._view.txt_result.controls.append(ft.Text(f"{listaNodi[i]} - {listaNodi[i+1]} con peso {self._model.grafo[listaNodi[i]][listaNodi[i+1]]["weight"]}"))
        self._view.update_page()


    def fillDD(self):
            ann = "200"
            for i in range(5, 10):
                anno = ann + str(i)
                self._view.dd_anno.options.append(ft.dropdown.Option(
                    text=anno))
            ann = "201"
            for i in range(0, 4):
                anno = ann + str(i)
                self._view.dd_anno.options.append(ft.dropdown.Option(
                    text=anno))
            citta=self._model.citta
            for c in citta:
                self._view.dd_citta.options.append(ft.dropdown.Option(
                    text=c))