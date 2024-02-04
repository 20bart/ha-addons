#coding: utf-8

'''
Tabelle di corrispondenza
	Il rango 0 corrisponde alla posizione dell'informazione nel frame MAESTRO
	Il rango 1 corrisponde al titolo pubblicato sul broker
	Il rango 2 (opzionale) permette di sostituire il codice del frame con un'informazione testuale corrispondente
'''
RecuperoInfo=[
	[1,"Stato della stufa",[
						[0, "Spento"],
						[1, "Controllo della stufa fredda / calda"],
						[2, "Pulizia Fredda"],
						[3, "Caricamento Freddo"],
						[4, "Avvio 1 Freddo"],
						[5, "Avvio 2 Freddo"],
						[6, "Pulizia Calda"],
						[7, "Caricamento Caldo"],
						[8, "Avvio 1 Caldo"],
						[9, "Avvio 2 Caldo"],
						[10, "Stabilizzazione"],
						[11, "Potenza 1"],
						[12, "Potenza 2"],
						[13, "Potenza 3"],
						[14, "Potenza 4"],
						[15, "Potenza 5"],
						[30, "Modalità diagnostica"],
						[31, "In funzione"],
						[40, "Spegnimento"],
						[41, "Raffreddamento in corso"],
						[42, "Pulizia bassa pot."],
						[43, "Pulizia alta pot."],
						[44, "Sblocco coclea"],
						[45, "AUTO ECO"],
						[46, "Standby"],
						[48, "Diagnostica"],
						[49, "CARIC. COCLEA"],
						[50, "Errore A01 - Accensione fallita"],
						[51, "Errore A02 - Nessuna fiamma"],
						[52, "Errore A03 - Surriscaldamento del serbatoio"],
						[53, "Errore A04 - Temperatura dei fumi troppo alta"],
						[54, "Errore A05 - Ostruzione condotto - Vent"],
						[55, "Errore A06 - Tiraggio insufficiente"],
						[56, "Errore A09 - Guasto sonda dei fumi"],
						[57, "Errore A11 - Guasto motoriduttore"],
						[58, "Errore A13 - Temperatura scheda madre troppo alta"],
						[59, "Errore A14 - Difetto attivo"],
						[60, "Errore A18 - Temperatura dell'acqua troppo alta"],
						[61, "Errore A19 - Guasto sonda temperatura acqua"],
						[62, "Errore A20 - Guasto sonda ausiliaria"],
						[63, "Errore A21 - Allarme pressostato"],
						[64, "Errore A22 - Guasto sonda ambiente"],
						[65, "Errore A23 - Guasto chiusura braciere"],
						[66, "Errore A12 - Guasto controllo motoriduttore"],
						[67, "Errore A17 - Intasamento coclea"],
						[69, "Attesa Allarmi sicurezza"],
						]],
	[2,"Stato del ventilatore ambiente",[
										[0, "Disattivato"],
										[1, "Livello 1"],
										[2, "Livello 2"],
										[3, "Livello 3"],
										[4, "Livello 4"],
										[5, "Livello 5"],
										[6, "Automatico"],
										]],
	[3,"Stato del ventilatore canalizzato 1",[
										[0, "Disattivato"],
										[1, "Livello 1"],
										[2, "Livello 2"],
										[3, "Livello 3"],
										[4, "Livello 4"],
										[5, "Livello 5"],
										[6, "Automatico"],
										]],
	[4,"Stato del ventilatore canalizzato 2",[
										[0, "Disattivato"],
										[1, "Livello 1"],
										[2, "Livello 2"],
										[3, "Livello 3"],
										[4, "Livello 4"],
										[5, "Livello 5"],
										[6, "Automatico"],
										]],
	[5,"Temperatura dei fumi"],
	[6,"Temperatura ambiente"],
	[7,"Temperatura Puffer"], # !=255 == Hydro
	[8,"Temperatura caldaia"],
	[9,"Temperatura NTC3"], # !=255 == Hydro
	[10,"Stato della candela",[
					[0, "Ok"],
					[1, "Usata"],
					]],
	[11,"ACTIVE - Set"],
	[12,"RPM - Ventilatore fumi"],
	[13,"RPM - Coclea - SET"],
	[14,"RPM - Coclea - LIVE"],
	[17,"Braciere",[
					[0, "OK"],
					[101, "Apertura braciere"],
					[100, "Chiusura braciere"],
					]], # !==Matic
	[18,"Profilo",[
					[0, "Manuale"],
					[1, "Dinamico"],
					[2, "Notturno"],
					[3, "Comfort"],
					[4, "Potenza 110%"],
					[10, "Modalità Adattiva"],
					]],
	[20,"Stato della modalità Active",[
					[0, "Off"],
					[1, "On"],
					]],  #0: Disattivato, 1: Attivato
	[21,"ACTIVE - Live"],
	[22,"Modalità di regolazione",[
							[0, "Manuale"],
							[1, "Dinamica"],
							]],
	[23,"Modalità ECO",[
					[0, "Off"],
					[1, "On"],
					]],
	[24,"Silenzioso",[
					[0, "Off"],
					[1, "On"],
					]],
	[25,"Modalità Cronotermostato",[
					[0, "Off"],
					[1, "On"],
					]],
	[26,"TEMP - Consigna"],
	[27,"TEMP - Caldaia"],
	[28,"TEMP - Scheda madre"],
	[29,"Potenza Attiva",[
							[11, "Potenza 1"],
							[12, "Potenza 2"],
							[13, "Potenza 3"],
							[14, "Potenza 4"],
							[15, "Potenza 5"],
							]],
	[32,"Ora della stufa (0-23)"],
	[33,"Minuti della stufa (0-29)"],
	[34,"Giorno della stufa (1-31)"],
	[35,"Mese della stufa (1-12)"],
	[36,"Anno della stufa"],
	[37,"Ore di funzionamento totali (s)"],
	[38,"Ore di funzionamento a potenza 1 (s)"],
	[39,"Ore di funzionamento a potenza 2 (s)"],
	[40,"Ore di funzionamento a potenza 3 (s)"],
	[41,"Ore di funzionamento a potenza 4 (s)"],
	[42,"Ore di funzionamento a potenza 5 (s)"],
	[43,"Ore prima della manutenzione"],
	[44,"Minuti prima dello spegnimento"],
	[45,"Numero di accensioni"],
	[47,"Sonda Pellet",[
						[0, "Sonda non attiva"],
						[10, "Livello sufficiente"],
						[11, "Livello quasi vuoto"],
						]],
	[48,"Effetto sonoro",[
					[0, "Off"],
					[1, "On"],
					]],
	[49,"Stato effetti sonori",[
					[0, "Off"],
					[1, "On"],
					]],
	[50,"Sleep",[
					[0, "Off"],
					[1, "On"],
					]],
	[51,"Modalità",[
				[0, "Inverno"],
				[1, "Estate"],
				]],
	[52,"Sonda wifi temperatura 1"],
	[53,"Sonda wifi temperatura 2"],
	[54,"Sonda wifi temperatura 3"],
	[55,"Sconosciuto"],
	[56,"Set Puffer"],
	[57,"Set Caldaia"],
	[58,"Set Health"], # !==Hydro
	[59,"Temperatura di ritorno"],
	[60,"Antigelo",[
					[0, "Off"],
					[1, "On"],
					]],
	]