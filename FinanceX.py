
from colorama import *
init();
while True:
	print(Fore.LIGHTGREEN_EX + "")
	print("\n  ____  *        ____         ____  ____      ____    ___")
	print(" |      | |\  | |    | |\  | |     |             __   __")
	print(" |----  | | \ | | -- | | \ | |     |--    ===      __   ") 
	print(" |      | |  \| |    | |  \| |____ |____      ___   ____      By: Erwin Ortiz")

	print("")
	print(Fore.LIGHTBLUE_EX + " *** MENU ***")
	print("")
	print(" ** ANALISIS DE UNA EMPRESA **\n")
	print(Fore.YELLOW + "    1.- " + Fore.LIGHTBLUE_EX + "Análisis General de Estados Financieros\n")
	print(" ** ANALISIS POR INDICADOR **\n")
	print(Fore.YELLOW + "    2.- " + Fore.LIGHTBLUE_EX + "Razón Corriente" + Fore.YELLOW + "   3.- " + Fore.LIGHTBLUE_EX + "Prueba Ácida" + Fore.YELLOW + "   4.- " + Fore.LIGHTBLUE_EX + "Rotación Inventario (veces)" + Fore.YELLOW + "   5.- " + Fore.LIGHTBLUE_EX + "Rotación Inventario (días)")
	print(Fore.YELLOW + "    6.- " + Fore.LIGHTBLUE_EX + "Rotación Cartera" + 	Fore.YELLOW + "   7.- " + Fore.LIGHTBLUE_EX + "Rotación Ctas. por Pagar (veces)" + Fore.YELLOW + "   8.- " + Fore.LIGHTBLUE_EX + "Rotación Ctas. por Pagar (días)") 
	print(Fore.YELLOW + "    9.- " + Fore.LIGHTBLUE_EX + "Razón de Endeudamiento" + Fore.YELLOW + "   10.- " + Fore.LIGHTBLUE_EX + "Razón Pasivo/Capital" + Fore.YELLOW + "   11.- " + Fore.LIGHTBLUE_EX + "Rendimiento sobre activos" + Fore.YELLOW + "   12.- " + Fore.LIGHTBLUE_EX + "Rotación de Activos")
	print(Fore.YELLOW + "    13.- " + Fore.LIGHTBLUE_EX + "Utilidad por Acción\n")

	print(" ** OTRAS HERRAMIENTAS **\n")
	print(Fore.YELLOW + "    14.- " + Fore.LIGHTBLUE_EX + "Tabla de Amortización (método francés)" + Fore.YELLOW + "   15.- " + Fore.LIGHTBLUE_EX + "Valor Presente" + Fore.YELLOW + "   16.- " + Fore.LIGHTBLUE_EX + "Valor Futuro " + Fore.YELLOW + "   17.- " + Fore.LIGHTBLUE_EX + " Z-Score")

	try:
		print(Fore.LIGHTGREEN_EX + "\n")
		seleccion= int(input("    Selecciona una opción --->: "))
		print(Fore.WHITE + "")
	except ValueError:
		print(Fore.LIGHTRED_EX + ".\n   *** Debes escribir un numero ***: ")
		continue

	if seleccion ==1 :

#AQUI SE REGISTRAN LAS VARIABLES DEL ACTIVO
		print(Fore.LIGHTBLUE_EX + "Registra los datos del Activo:") 
		print(Fore.WHITE +"")
		ac= float(input("  Activo Corriente:    $ "))
		anc= float(input("  Activo No Corriente: $ "))
		inv= float(input("  Inventario:          $ "))
		inv_i= float(input("      Inventario Inicial:  $ "))
		inv_f= float(input("      Inventario Final:    $ "))
		cxc= float(input("  Ctas por Cob. Clientes:  $ "))
		cxc_si= float(input("    Saldo Inic. CxC:       $ "))
		cxc_sf= float(input("    Saldo Fin. CxC:        $ "))
		afx= float(input("  Activos Fijos:       $ "))
		print("")
		print(Fore.LIGHTBLUE_EX + "Registra los datos del Pasivo y Patrimonio: ")
		print(Fore.WHITE +"")

#AQUI SE REGISTRAN LAS VARIABLES DEL PASIVO Y PATRIMONIO
		pc= float(input("  Pasivo Corriente:    $ "))
		cxp_si= float(input("   Saldo In.  CxP Proveed: $ "))
		cxp_sf= float(input("   Saldo Fin. CxP Proveed: $ "))
		pnc= float(input("  Pasivo no Corriente: $ "))
		pres_cp= float(input("  Prést. C. Plazo:     $ "))
		pres_lp= float(input("  Prést. L. Plazo:     $ "))
		num_accs= int(input("  # Accs. en Circ.:    $ "))
		patrimonio= float(input("  Patrimonio:        $ "))
		print("")


		print(Fore.LIGHTBLUE_EX + "Registra los datos del Estado de Resultados: ")
		print(Fore.WHITE +"")

# AQUI SE REGISTRAN LAS VARIABLES DEL ESTADO DE RESULTADOS
		#vtot= float(input("  Ventas Totales:      $ "))
		vtcred= float(input("  Ventas a Crédito:    $ "))
		vtcont= float(input("  Ventas al Contado:   $ "))
		costvta= float(input("  Costos Totales:      $ "))
		ebit= float(input("  EBIT:                $ "))
		ebitda= float(input("  EBITDA:              $ "))
		utilnet= float(input("  Utilidad Neta:       $ "))
		costfin= float(input("  Gtos Financieros:    $ "))
		print("")
	
# CALCULOS DE RAZONES FINANCIERAS
		print(Fore.LIGHTMAGENTA_EX + " RAZONES DE LIQUIDEZ: \n")
		print(Fore.LIGHTRED_EX + "  Razón Corriente:  #  ", round((ac/pc),2))
		print("  Prueba Ácida:     #  ", round(((ac-inv)/pc),2))
		print("  Rot. Inventarios: #  ", round(costvta/((inv_i+inv_f)/2),2))
		print("  Rot. Inventarios: dias", round(365/(costvta/((inv_i+inv_f)/2)),2))
		print("  Rot. de cartera:  dias", round(365/(vtcred/((cxc_si+cxc_sf)/2)),2))
		print("  Rot. Ctas. x Pag: #  ", round(costvta/((cxp_si+cxp_sf)/2),2))
		print("  Rot. Ctas. x Pag: dias", round(365/(costvta/((cxp_si+cxp_sf)/2)),2))
		print("")
		print(Fore.LIGHTMAGENTA_EX + " RAZONES DE DEUDA: \n")
		print(Fore.LIGHTRED_EX + "  Razón Endeuda:    %  ", round(((pc+pnc)/(ac+anc))*100,2))
		print("  Pasivo/Capital:   #  ", round((pres_lp/patrimonio),2))
		print("")
		print(Fore.LIGHTMAGENTA_EX + "  RAZONES DE RENTABILIDAD: \n")
		print(Fore.LIGHTRED_EX + "  Rendim/activos (ROA):  %  ", round(((utilnet+costfin)/(ac+anc)*100),2))
		print("   Rotación de Activos:  #  ", round(((vtcred+vtcont)/(ac+anc)),2))
		print("  Utilidad x Acción:  $", round(((utilnet/num_accs)*100),2))

	elif seleccion ==2 :
		ac= float(input("               Activo Corriente:    $ "))
		pc= float(input("               Pasivo Corriente:    $ "))
		print(Fore.LIGHTRED_EX + "               Razón Corriente:  #  ", round((ac/pc),2))

	elif seleccion ==3 :
		ac= float(input("               Activo Corriente:    $ "))
		inv= float(input("               Inventario:          $ "))
		pc= float(input("               Pasivo Corriente:    $ "))
		print(Fore.LIGHTRED_EX +"               Prueba Ácida:     #  ", round(((ac-inv)/pc),2))		

	elif seleccion ==4 :
		costvta= float(input("               Costos Totales:      $ "))
		inv_i= float(input("               Inventario Inicial:  $ "))
		inv_f= float(input("               Inventario Final:    $ "))
		print(Fore.LIGHTRED_EX +"               Rot. Inventarios: #  ", round(costvta/((inv_i+inv_f)/2),2))

	elif seleccion ==5 :
		costvta= float(input("               Costos Totales:      $ "))
		inv_i= float(input("               Inventario Inicial:  $ "))
		inv_f= float(input("               Inventario Final:    $ "))
		print(Fore.LIGHTRED_EX +"              Rot. Inventarios: dias", round(365/(costvta/((inv_i+inv_f)/2)),2))

	elif seleccion ==6 :
		vtcred= float(input("               Ventas a Crédito:    $ "))
		cxc_si= float(input("               Saldo Inic. CxC:       $ "))
		cxc_sf= float(input("               Saldo Fin. CxC:        $ "))
		print(Fore.LIGHTRED_EX +"               Rot. de cartera:  dias", round(365/(vtcred/((cxc_si+cxc_sf)/2)),2))

	elif seleccion ==7 :
		costvta= float(input("               Costos Totales:      $ "))
		cxp_si= float(input("               Saldo In.  CxP Proveed: $ "))
		cxp_sf= float(input("               Saldo Fin. CxP Proveed: $ "))
		print(Fore.LIGHTRED_EX +"               Rot. Ctas. x Pag: #  ", round(costvta/((cxp_si+cxp_sf)/2),2))

	elif seleccion ==8 :
		costvta= float(input("               Costos Totales:      $ "))
		cxp_si= float(input("               Saldo In.  CxP Proveed: $ "))
		cxp_sf= float(input("               Saldo Fin. CxP Proveed: $ "))
		print(Fore.LIGHTRED_EX +"               Rot. Ctas. x Pag: dias", round(365/(costvta/((cxp_si+cxp_sf)/2)),2))

	elif seleccion ==9 :
		pc= float(input("               Pasivo Corriente:    $ "))
		pnc= float(input("               Pasivo no Corriente: $ "))
		ac= float(input("               Activo Corriente:    $ "))
		anc= float(input("               Activo No Corriente: $ "))
		print(Fore.LIGHTRED_EX + "               Razón Endeuda:    %  ", round(((pc+pnc)/(ac+anc))*100,2))

	elif seleccion ==10 :
		pres_lp= float(input("               Prést. L. Plazo:     $ "))
		patrimonio= float(input("               Patrimonio:        $ "))
		print(Fore.LIGHTRED_EX +"               Pasivo/Capital:   #  ", round((pres_lp/patrimonio),2))

	elif seleccion ==11 :
		utilnet= float(input("               Utilidad Neta:       $ "))
		costfin= float(input("               Gtos Financieros:    $ "))
		ac= float(input("               Activo Corriente:    $ "))
		anc= float(input("               Activo No Corriente: $ "))
		print(Fore.LIGHTRED_EX + "               Rendim/activos (ROA):  %  ", round(((utilnet+costfin)/(ac+anc)*100),2))

	elif seleccion ==12 :
		vtcred= float(input("               Ventas a Crédito:    $ "))
		vtcont= float(input("               Ventas al Contado:   $ "))
		ac= float(input("               Activo Corriente:    $ "))
		anc= float(input("               Activo No Corriente: $ "))
		print(Fore.LIGHTRED_EX +"               Rotación de Activos:  #  ", round(((vtcred+vtcont)/(ac+anc)),2))

	elif seleccion ==12 :
		utilnet= float(input("               Utilidad Neta:       $ "))
		num_accs= int(input("               # Accs. en Circ.:    $ "))
		print(Fore.LIGHTRED_EX +"               Utilidad x Acción:  $", round(((utilnet/num_accs)*100),2))

	elif seleccion ==14 :
		credito= float(input("   Ingrese el valor del crédito:                $ "))
		tasa= float(input("   Ingrese la tasa de interés:                  %  "))
		plazo= int(input("   Ingrese los meses para amortizar el préstamo:   "))

		tasa= (tasa/100)/12
		interes= credito * tasa
		cuota= credito * (((1+tasa)**plazo)*tasa/((1+tasa)**plazo-1))

		print("\n     -------RESUMEN-------")
		print("\n     Cuota Mensual:   $"  , round(cuota,2))
		print("     Interes Mensual: $  " , round(interes,2))
		print(Fore.LIGHTMAGENTA_EX + "\n -----------", " -------------", "-------------------", "  -------------", "  ------------")
		print(Fore.WHITE + "\n   PLAZO     |  INTERES    |   ABONO A CAPITAL   |    CUOTA     |     SALDO \n" )
		print(Fore.LIGHTMAGENTA_EX + " -----------", " -------------", "-------------------", "  -------------", "  ------------\n")
		for i in range(plazo):
			interes = credito * tasa
			print(Fore.WHITE + "   mes ", (i+1), " --->  "  ,  round(interes, 2) , " --->     " , round(cuota-interes,2) , " ----->    ", round(cuota,2) , "--->   ", round(credito-(cuota-interes),2))
			credito -= cuota - interes

	elif seleccion ==15 :
		print(Fore.YELLOW + "    1. " + Fore.LIGHTBLUE_EX + "Para cálculo de valor presente simple " + Fore.YELLOW + "   2. " + Fore.LIGHTBLUE_EX + " Para cálculo de valor presente de una anualidad \n ")
		print(Fore.LIGHTGREEN_EX + "")
		altern = int(input("    Elija opción ----> : "))
		if altern == 1 :
			print(Fore.WHITE + "")
			vf= float(input("\n    Ingresa el valor futuro:                 $ "))
			r = float(input("    Ingresa la tasa de interés anual:        % "))
			t = float(input("    Ingresa el numero de periodos (meses):   # "))
			if t == 12 :
				vp =  vf / ((1 + ((r/100)))**1)
			elif  t != 12 :
				vp =  vf / ((1 + ((r/100)/12))**t)
			print(Fore.LIGHTRED_EX + "    El valor presente es :                   $ ", round(vp,2))
		elif altern == 2 :
			print(Fore.WHITE + "")
			vf= float(input("\n   Ingresa el valor futuro:    $ "))
			r = float(input("   Ingresa la tasa de interés: % "))
			n = int(input("   Periodo de capitalización: 1.- mensual, 2.- bimestral, 3.- trimestral, 4.- semestral, 5.- anual : "))
			t = float(input("   Ingresa el numero de periodos (meses): # "))

			if n == 1 :
				vp =  vf / ((1 + ((r/100)))**t)
				print(Fore.LIGHTRED_EX + "   El valor presente es : $ ", round(vp,2))

			elif n == 2 :
				vp = vf / ((1 + ((r/100)/6))**(t/2))
				print(Fore.LIGHTRED_EX + "   El valor presente es : $ ", round(vp,2))

			elif n == 3 :
				vp = vf / ((1+((r/100)/4))**(t/3))
				print(Fore.LIGHTRED_EX + "   El valor presente es : $ ", round(vp,2))

			elif n == 4 :
				vp = vf / ((1+((r/100)/2))**(t/6))
				print(Fore.LIGHTRED_EX + "   El valor presente es : $ ", round(vp,2))

			elif n == 5 :
				vp = vf / ((1+((r/100)/1))**(t/12))
				print(Fore.LIGHTRED_EX + "   El valor presente es: $ ", round(vp,2))

			
	elif seleccion == 16 :
		print(Fore.YELLOW + "    1. " + Fore.WHITE + "Para cálculo de valor futuro simple " + Fore.YELLOW + "   2. " + Fore.WHITE + " Para cálculo de valor futuro de una anualidad \n \n")
		altern2 = int(input("   Elija opción: "))
		if altern2 == 1 :
			vp= float(input("\n    Ingresa el valor presente:              $ "))
			r = float(input("    Ingresa la tasa de interés anual:       %    "))
			t = float(input("    Ingresa el numero de periodos (meses):  #    "))
			if t == 12 :
				vf =  vp * ((1 + ((r/100)))**1)
			elif  t != 12 :
				vf =  vp * ((1 + ((r/100)/12))**t)
			print(Fore.LIGHTRED_EX + "    El valor futuro es : $                   ", round(vf,2))

		elif altern2 == 2 :
			vp= float(input("\n   Ingresa el valor presente:    $ "))
			r = float(input("   Ingresa la tasa de interés: % "))
			n = int(input("   Periodo de capitalización: 1.- mensual, 2.- bimestral, 3.- trimestral, 4.- semestral, 5.- anual : "))
			t = float(input("   Ingresa el numero de periodos (meses): # "))

			if n == 1 :
				vf =  vp * ((1 + ((r/100)))**t)
				print(Fore.LIGHTRED_EX + "   El valor futuro es : $ ", round(vf,2))

			elif n == 2 :
				vf = vp * ((1 + ((r/100)/6))**(t/2))
				print(Fore.LIGHTRED_EX + "   El valor futuro es : $ ", round(vf,2))

			elif n == 3 :
				vf = vp * ((1+((r/100)/4))**(t/3))
				print(Fore.LIGHTRED_EX + "   El valor futuro es : $ ", round(vf,2))

			elif n == 4 :
				vf = vp * ((1+((r/100)/2))**(t/6))
				print(Fore.LIGHTRED_EX + "   El valor futuro es : $ ", round(vf,2))

			elif n == 5 :
				vf = vp * ((1+((r/100)/1))**(t/12))
				print(Fore.LIGHTRED_EX + "   El valor futuro es: $ ", round(vf,2))


	elif seleccion == 17 :
		print (Fore.YELLOW + "   1.-" + Fore.LIGHTBLUE_EX + " La empresa cotiza en bolsa" + Fore.YELLOW + "   2.-" + Fore.LIGHTBLUE_EX + " La empresa no cotiza en bolsa\n")
		print(Fore.LIGHTGREEN_EX + "")
		z_altman = int(input("      Elija opción ----> : "))
		if z_altman == 1 :
			print(Fore.WHITE + "")
			AC_Z = float(input("\n      Total de Activos Corrientes:      $ "))
			ACT_Z = float(input("      Activos Totales:                  $ "))
			PC_Z = float(input("      Total de Pasivos Corrientes:      $ "))
			PAST_Z = float(input("      Total de Pasivos:                 $ "))
			ACCS_Z = int(input("      Total de acciones:                # "))
			PRECIO_Z = float(input("      Precio de la acción en el mercado:$ "))
			UTRET_Z= float(input("      Total de Utilidades Retenidas:    $ "))
			VT_Z = float(input("      Total de Ventas:                  $ "))
			IMP_Z = float(input("      Total de impuestos:               $ "))
			INT_Z = float(input("      Total de intereses:               $ "))
			PART_Z = float(input("      Participación de trabajadores:    $ "))
			UT_Z = float(input("      Utilidad neta:                    $ "))

			X1 = (AC_Z - PC_Z) / ACT_Z
			X2 = UTRET_Z / ACT_Z
			X3 = (UT_Z + PART_Z + INT_Z + IMP_Z) / ACT_Z
			X4 = (ACCS_Z * PRECIO_Z) / PAST_Z 
			X5 = VT_Z / ACT_Z
			Z = (1.2 * X1) + (1.4 * X2) + (3.3 * X3) + (0.6 * X4) + (0.99 * X5)
			if Z > 2.99 :
				print(Fore.LIGHTGREEN_EX + "\n")
				print("      Z DE ALTMAN = ", round(Z,2))
				print ("      La empresa está saludable financieramente")
			elif Z > 1.8 and Z1 < 2.1 :
				print(Fore.LIGHTMAGENTA_EX + "\n")
				print("      Z DE ALTMAN = ", round(Z,2))
				print("      Alerta: Posibilidad de quiebra en los próximos 2 años")
			elif Z < 1.8 :
				print(Fore.LIGHTRED_EX + "\n")
				print("      Z DE ALTMAN = ", round(Z,2))
				print("      ALERTA: PROBABILIDAD MUY ALTA DE QUIEBRA")

		elif z_altman == 2 :
			print (Fore.YELLOW + "\n      1.-" + Fore.LIGHTBLUE_EX + " Es una empresa INDUSTRIAL" + Fore.YELLOW + "    2.-" + Fore.LIGHTBLUE_EX + " Es una empresa COMERCIAL")
			print(Fore.LIGHTGREEN_EX + "")
			z_altman_sel = int(input("\n      Elija opción ----> : "))
			if z_altman_sel == 1 :
				print(Fore.WHITE + "")
				AC_Z1 = float(input("\n      Total de Activos Corrientes:      $ "))
				ACT_Z1 = float(input("      Activos Totales:                  $ "))
				PC_Z1 = float(input("      Total de Pasivos Corrientes:      $ "))
				PAST_Z1 = float(input("      Total de Pasivos:                 $ "))
				PA_Z1 = float(input("      Total Patrimonio:                 $ "))
				UTRET_Z1= float(input("      Total de Utilidades Retenidas:    $ "))
				VT_Z1 = float(input("      Total de Ventas:                  $ "))
				IMP_Z1 = float(input("      Total de impuestos:               $ "))
				INT_Z1 = float(input("      Total de intereses:               $ "))
				PART_Z1 = float(input("      Participación de trabajadores:    $ "))
				UT_Z1 = float(input("      Utilidad neta:                    $ "))

				X1= (AC_Z1 - PC_Z1) / ACT_Z1
				X2 = UTRET_Z1 / ACT_Z1
				X3 = (UT_Z1 + PART_Z1 + INT_Z1 + IMP_Z1) / ACT_Z1
				X4 = PA_Z1 / PAST_Z1
				X5 = VT_Z1 / ACT_Z1
				Z1 = (0.717 * X1) + (0.847 * X2) + (3.107 * X3) + (0.42 * X4) + (0.998 * X5)
				if Z1 > 3 :
					print(Fore.LIGHTGREEN_EX + "\n")
					print("      Z1 DE ALTMAN = ", round(Z1,2))
					print ("      La empresa está saludable financieramente")
				elif Z1 > 2.7 and Z1 < 3.0 :
					print(Fore.YELLOW + "\n")
					print("      Z1 DE ALTMAN = ", round(Z1,2))
					print("      Alerta: Actuar con cautela para no caer en Zona Gris")
				elif Z1 >1.8 and Z1 < 2.7 :
					print(Fore.LIGHTMAGENTA_EX)
					print("      Z1 DE ALTMAN = ", round(Z1,2))
					print("      Alerta: Posibilidad de quiebra en los próximos 2 años")
				elif Z1 < 1.8 :
					print(Fore.LIGHTRED_EX + "\n")
					print("      Z1 DE ALTMAN = ", round(Z1,2))
					print("      ALERTA: PROBABILIDAD MUY ALTA DE QUIEBRA")

			if z_altman_sel == 2 :
				AC_Z2 = float(input("\n      Total de Activos Corrientes:      $ "))
				ACT_Z2 = float(input("      Activos Totales:                  $ "))
				PC_Z2 = float(input("      Total de Pasivos Corrientes:      $ "))
				PAST_Z2 = float(input("      Total de Pasivos:                 $ "))
				PA_Z2 = float(input("      Total Patrimonio:                 $ "))
				UTRET_Z2= float(input("      Total de Utilidades Retenidas:    $ "))
				VT_Z2 = float(input("      Total de Ventas:                  $ "))
				IMP_Z2 = float(input("      Total de impuestos:               $ "))
				INT_Z2 = float(input("      Total de intereses:               $ "))
				PART_Z2 = float(input("      Participación de trabajadores:    $ "))
				UT_Z2 = float(input("      Utilidad neta:                    $ "))

				X1 = (AC_Z2 - PC_Z2) / ACT_Z2
				X2 = UTRET_Z2 / ACT_Z2
				X3 = (UT_Z2 + PART_Z2 + INT_Z2 + IMP_Z2) / ACT_Z2
				X4 = PA_Z2 / PAST_Z2
				Z2 = (6.56 * X1) + (3.267 * X2) + (6.72 * X3) + (1.05242 * X4)
				if Z2 > 2.6 :
					print(Fore.LIGHTGREEN_EX + "\n")
					print("      Z2 DE ALTMAN = ", round(Z2,2))
					print ("      La empresa está saludable financieramente")
				elif Z2 > 1.1 and Z2 < 2.6 :
					print(Fore.LIGHTMAGENTA_EX + "\n")
					print("      Z2 DE ALTMAN = ", round(Z2,2))
					print("      Alerta: Posibilidad de quiebra en los próximos 2 años")
				elif Z2 < 1.1 :
					print("\n      Z2 DE ALTMAN = ", round(Z2,2))
					print(Fore.LIGHTRED_EX + "      ALERTA: PROBABILIDAD MUY ALTA DE QUIEBRA")


	elif seleccion >17 :
				print(Fore.LIGHTRED_EX + "   *** Debes Ingresar una opción disponible*** ")

	else:
		break



	



