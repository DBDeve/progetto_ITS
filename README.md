# progetto_ITS
NOME PROGETTO: G_agr



DESCRIZIONE PROGETTO:
Il progetto consiste nella creazione di una web app che aiuti i proprietari di agriturismi a gestire ogni aspetto della loro azienda. 

Nello specifico il programma si occupera di gestire clienti lavoratori entrate, uscite e soprattuto gli agriturismi e le varie attività legate ad essi es: camere, ristoranti ecc...
il progetto si propone come un programma gratuito di base, ma che per delle funzionalità in più richiede un pagamento.

Problem: l'incapacità degli agriturismi di tenere sotto controllo le entrate le uscite e le varie attività delle loro aziende

Solution: Un programma che riesce a tenere traccia delle entrate e le uscite di tutte le attività 

Unique value proposition: Dal momento che un agriturismo può essere composto da varie attività e alcune possono non esserci il programma chiederà ai nuovi utenti delle domande e in base a quelle permetterà di inserire dati in un modello o meno. Ad esempio se un nuovo gestore dice che il suo agriturismo non possiede un ristorante il programma non gli permetterà di inserire alcun dato all'interno della tabella restaurants




INFORMAZIONI UTILIZZO DELLA REPO: 

COMANDI PRINCIPALI 
Per la verifica del funzionamento è necassario prima attivare il venv tramite il comando: source .venv/bin/activate

dopodiché è necessario avviare il server in locale attraverso il comando: python manage.py runserver

Nel caso si rendesse necessario andare sull'amministrazione di Django è necessario creare un superuser. ecco il procedimento:
1) usare il comando: python manage.py createsuperuser
2) inserire nome utente
3) inserire mail
4) inserire password. i caratteri inseriti non verranno mostrati. è possibile anche non inserire alcun carattere; in quel caso il programma chiederà conferma. premere y per confermare.

per la modifica del file models.py è necessario usare in requenza i comandi "python manage.py makemigrations" e "python manage.py migrate"
python manage.py makemigrations: crea altri file che si occupano della modifica dei dati in models.py
python manage.py migrate: esegue i programmi creati con il comando precedente

INFORMAZIONI PER LE MODIFICHE 

Nel caso sia necessario operare una ristrutturazione dei modelli e necessario cancellare prima le migrazioni nella cartella migrations




FUNZIONALITA' DA SVILUPPARE IN FUTURO:
•	implementare una schermata per la modifica delle impostazione dell'utente (sia clienti che gestore).
• implementare una schermata per il cambio password
• creare un'applicazione clienti in cui gli utenti possano sia registrarsi, sia prenotare in eventuali alberghi e ristoranti degli agriturismi.
•	creare una funzione che prende i dati dalla tabella stipendi e lavoratori e da quelli crei un nuovo oggetto Spese con i dati del lavoratore e del relativo stipendio.
•	Creare una funzione che cambia lo stato delle camere in base a se ha assegnato un cliente o no. Quando il cliente viene associato lo stato viene impostato su occupato, quando il cliente viene dissociato lo stato viene impostato su libera.



CODICE FUNZIONANTE:
•Il programma è in grado di registrare gli utenti e permette loro di effettuare sia il login che il logout. 
•Se qualcuno cerca di accedere ai dati di un'utente passando un url con il suo username senza aver effetuato l'accesso il programma lo ritrasporta alla pagina di login.
•la funzione visualizza() è funzionante e stampa soltanto i dati collegato a uno specifico account (quello che ha effettuato il login).
•le funzione modifica(), aggiungi() e elimina() prendono ancora tutti gli oggetti senza filtrare per l'account. 
•il codice della grafica richiede una ristrutturazione. necessario inserimeto footer e cambio grafica header

