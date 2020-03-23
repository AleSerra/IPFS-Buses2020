# IPFS-Buses2020
Di seguito la descrizione dei vari script e cartelle presenti:
#### JavaScript
- <b>ipfsSiaTest.js</b>: Script JavaScript per testare l'upload dei dati contenuti all'interno del file "<i>inputDataset1.csv</i>" sia su rete IPFS sia su rete SkyNet
- <b>bigFileIpfsSiaTest.js</b>: Script JavaScript per testare l'upload dei file di dimensioni variabili contenuti nella cartella "<i>bigfile</i>" sia su rete IPFS sia su rete SkyNet
- <b>downloadTest.js</b>: Script Javascript per effettuare i test di download dei file caricati sulla rete in precedenza dallo script "<i>bigFileIpfsSiaTest.js</i>", effettua i test sia su rete Skynet e sia su rete IPFS
#### Python
- <b>bigFileGraph.py</b>: Script Python utile per  effettuare la rappresentazione dello use case <i>Caricamento di fie di grandi dimensioni</i>. Prende i file presenti nella cartella <i>bigfiletests</i> e li rappresenta graficamente.
- <b>downloadGraph.py</b>: Script Python utile per  effettuare la rappresentazione dello use case <i>Download di fie di grandi dimensioni</i>. Prende i file presenti nella cartella <i>downtests</i> e li rappresenta graficamente.
- <b>graphIpfsSiaTest.py</b>: Script Python utile per  effettuare la rappresentazione dello use case <i>Caricamento delle informazioni della rete bus della città di Rio de Janeiro</i>. Prende i file presenti nella cartella <i>tests</i> e <i>testsSia</i>  e li rappresenta graficamente.

#### Cartelle
- <b>/bigfile</b>: Cartella contenente i file di esempio per lo script "<i>bigFileIpfsSiaTest.js</i>"
- <b>/bigfiletests</b>: Cartella contenente i risultati dei test ottenuti dallo script "<i>bigFileIpfsSiaTest.js</i>", divisi per rete IPFS e rete SkyNet
- <b>/dataset</b>: Cartella contenente i dataset di partenza con le informazioni delle fermate dei bus di Rio
- <b>/download</b>: Cartella contenente i file scaricati dallo script "<i>downloadTest.js</i>"
- <b>/downtests</b>: Cartella contenente i risultati dei test ottenuti dallo script "<i>downloadTest.js</i>", divisi per rete IPFS e rete SkyNet
- <b>/grafici</b>: Cartella contenente i grafici risultanti dall'esecuzione degli script Python. Contiene 3 sottocartelle, una per ogni tipologia di test effettuato. Ogni sottocartella contiene altre due sottocartelle per ogni tipologia di calcolo rappresentato attraverso i grafici
- <b>/tests</b>: Cartella contenente i risultati dei test ottenuti tramite lo script "<i>ipfsSiaTest.js</i>" su rete IPFS
- <b>/testsSia</b>: Cartella contenente i risultati dei test ottenuti tramite lo script "<i>ipfsSiaTest.js</i>" su rete SkyNet

