from forum.models import Foro,Comentario,Like
from entrys.models import Year, Modulo,Semana,Contenido,Evento,Ejercicio,Opciones
from Usuarios.models import Curso,Tema,Usuario,Grupo,Calificacion
from django.utils import timezone
import datetime

# # # CREAR EL AÑO Y LOS CURSOS CORRESPONDIENTES 

actYear = Year.objects.create(year=2023)

curso10_1 = Curso.objects.create(nombre_curso="10_1",grado=10,year=actYear)
curso10_2 = Curso.objects.create(nombre_curso="10_2",grado=10,year=actYear)
curso10_3 = Curso.objects.create(nombre_curso="10_3",grado=10,year=actYear)
curso10_4 = Curso.objects.create(nombre_curso="10_4",grado=10,year=actYear)

actYear.save();curso10_1.save();curso10_2.save();curso10_3.save();curso10_4.save()


curso11_1 = Curso.objects.create(nombre_curso="11_1",grado=10,year=actYear)
curso11_2 = Curso.objects.create(nombre_curso="11_2",grado=10,year=actYear)
curso11_3 = Curso.objects.create(nombre_curso="11_3",grado=10,year=actYear)
curso11_4 = Curso.objects.create(nombre_curso="11_4",grado=10,year=actYear)

curso11_1.save();curso11_2.save();curso11_3.save();curso11_4.save()

# # # CREAR LOS MODULOS Y LAS SEMANAS

mod1 = Modulo.objects.create(tituloMod="Introduction",year=actYear)
mod2 = Modulo.objects.create(tituloMod="What is research and its importance",year=actYear)
mod3 = Modulo.objects.create(tituloMod="Choosing the subject for your EE",year=actYear)
mod4 = Modulo.objects.create(tituloMod="Monograph development",year=actYear)

mod1.save();mod2.save();mod3.save(),mod4.save()


# # # CREAR LAS SEMANAS

Sem1 = Semana.objects.create(tituloSem='1',seman=1,modulo=mod1)
# Sem2 = Semana.objects.create(tituloSem='2',seman=2,modulo=mod1)
# Sem3 = Semana.objects.create(tituloSem='3',seman=3,modulo=mod1)
# Sem4 = Semana.objects.create(tituloSem='4',seman=4,modulo=mod1)
# Sem5 = Semana.objects.create(tituloSem='5',seman=5,modulo=mod1)
# Sem6 = Semana.objects.create(tituloSem='6',seman=6,modulo=mod1)
# Sem7 = Semana.objects.create(tituloSem='7',seman=7,modulo=mod1)
# Sem8 = Semana.objects.create(tituloSem='8',seman=8,modulo=mod1)
# Sem9 = Semana.objects.create(tituloSem='9',seman=9,modulo=mod1)
# Sem10 = Semana.objects.create(tituloSem='10',seman=10,modulo=mod1)
Sem11 = Semana.objects.create(tituloSem='11',seman=11,modulo=mod2)
# Sem12 = Semana.objects.create(tituloSem='12',seman=12,modulo=mod2)
# Sem13 = Semana.objects.create(tituloSem='13',seman=13,modulo=mod2)
# Sem14 = Semana.objects.create(tituloSem='14',seman=1,modulo=mod2)
# Sem15 = Semana.objects.create(tituloSem='15',seman=1,modulo=mod2)
# Sem16 = Semana.objects.create(tituloSem='16',seman=1,modulo=mod2)
# Sem17 = Semana.objects.create(tituloSem='17',seman=1,modulo=mod2)
# Sem18 = Semana.objects.create(tituloSem='18',seman=1,modulo=mod2)
# Sem19 = Semana.objects.create(tituloSem='19',seman=1,modulo=mod2)
# Sem20 = Semana.objects.create(tituloSem='20',seman=1,modulo=mod2)
Sem21 = Semana.objects.create(tituloSem='21',seman=21,modulo=mod3)
# Sem22 = Semana.objects.create(tituloSem='22',seman=1,modulo=mod3)
# Sem23 = Semana.objects.create(tituloSem='23',seman=1,modulo=mod3)
# Sem24 = Semana.objects.create(tituloSem='24',seman=1,modulo=mod3)
# Sem25 = Semana.objects.create(tituloSem='25',seman=1,modulo=mod3)
# Sem26 = Semana.objects.create(tituloSem='26',seman=1,modulo=mod3)
# Sem27 = Semana.objects.create(tituloSem='27',seman=1,modulo=mod3)
# Sem28 = Semana.objects.create(tituloSem='28',seman=1,modulo=mod3)
# Sem29 = Semana.objects.create(tituloSem='29',seman=1,modulo=mod3)
# Sem30 = Semana.objects.create(tituloSem='30',seman=1,modulo=mod3)
Sem31 = Semana.objects.create(tituloSem='31',seman=31,modulo=mod4)
# Sem32 = Semana.objects.create(tituloSem='32',seman=1,modulo=mod4)
# Sem33 = Semana.objects.create(tituloSem='33',seman=1,modulo=mod4)
# Sem34 = Semana.objects.create(tituloSem='34',seman=1,modulo=mod4)
# Sem35 = Semana.objects.create(tituloSem='35',seman=1,modulo=mod4)
# Sem36 = Semana.objects.create(tituloSem='36',seman=1,modulo=mod4)
# Sem37 = Semana.objects.create(tituloSem='37',seman=1,modulo=mod4)
# Sem38 = Semana.objects.create(tituloSem='38',seman=1,modulo=mod4)
# Sem39 = Semana.objects.create(tituloSem='39',seman=1,modulo=mod4)
# Sem40 = Semana.objects.create(tituloSem='40',seman=1,modulo=mod4)

Sem1.save();Sem11.save();Sem21.save(),Sem31.save()

# # # CREAR EVENTOS PARA CADA SEMANA (se crearon 2 eventos para semana 1,
# # # y para sem 11,21,31, 1 evento para cada una)

Even1= Evento.objects.create(nombre="First Work Boys",semana = Sem1,comentario='''Lorem ipsum 
dolor sit amet, consectetur adipiscing elit. 
Sed imperdiet hendrerit odio, vel dignissim mi pretium non. Nam odio nunc, blandit 
non quam eget, fermentum ornare leo. 
Proin consequat tincidunt rhoncus. Aliquam tempus vulputate nisi vitae tincidunt. 
Vestibulum consequat, libero eget tincidunt varius, elit neque ornare nulla,
 quis malesuada magna tortor non tortor. Sed egestas magna porttitor libero 
 tristique, vitae gravida nunc scelerisque. Nullam enim eros, tempus non dapibus 
 vehicula, porttitor et sem. Nulla massa est, rhoncus nec rhoncus at, consectetur sit amet 
 augue. Duis non tempor arcu. Aenean lacinia sem ac maximus consequat. Integer in ultrices quam.
   Quisque sed leo laoreet, tempor risus ac, consequat purus.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames 
ac turpis egestas. Vivamus accumsan ultricies augue, suscipit imperdiet ex ultricies 
eu. Integer tincidunt efficitur dignissim. Nulla ultrices nibh tortor, 
vel elementum nibh fermentum eget. Sed quis dictum dui. Maecenas condimentum 
imperdiet interdum. Mauris pretium at risus bibendum commodo. Mauris dolor sem, 
sagittis id odio pretium, viverra vulputate erat. Nam id pulvinar magna, quis euismod 
risus. Sed commodo ipsum sed arcu consectetur fermentum. Orci varius natoque penatibus 
et magnis dis parturient montes, nascetur ridiculus mus. Integer malesuada sollicitudin
 ex, vel porttitor metus tempor at. Morbi tempus, lectus eu fermentum scelerisque, 
 libero dolor efficitur neque, sit amet euismod ex mi id nulla. Proin sit amet congue
   metus. Integer ac aliquam lorem, a tempor lacus. Nulla gravida, massa quis venenatis
     iaculis, nisl libero accumsan nulla, in tincidunt velit odio at urna.''', fecha=timezone.now(), 
     comentarioSimple='''Aliquam orci nibh, bibendum eget viverra id, lacinia non augue. 
     Aliquam viverra sodales arcu, ut placerat sem dictum sed. Suspendisse potenti. Fusce non 
     mollis orci. Aliquam consectetur dictum odio, id ornare elit tincidunt ut. Aliquam ultrices 
     sollicitudin lacus. Curabitur ultrices purus et blandit pharetra.''')

Even2= Evento.objects.create(nombre="11th Work Boys",semana = Sem11,comentario='''Lorem ipsum 
dolor sit amet, consectetur adipiscing elit. 
Sed imperdiet hendrerit odio, vel dignissim mi pretium non. Nam odio nunc, blandit 
non quam eget, fermentum ornare leo. 
Proin consequat tincidunt rhoncus. Aliquam tempus vulputate nisi vitae tincidunt. 
Vestibulum consequat, libero eget tincidunt varius, elit neque ornare nulla,
 quis malesuada magna tortor non tortor. Sed egestas magna porttitor libero 
 tristique, vitae gravida nunc scelerisque. Nullam enim eros, tempus non dapibus 
 vehicula, porttitor et sem. Nulla massa est, rhoncus nec rhoncus at, consectetur sit amet 
 augue. Duis non tempor arcu. Aenean lacinia sem ac maximus consequat. Integer in ultrices quam.
   Quisque sed leo laoreet, tempor risus ac, consequat purus.
ismod 
risus. Sed commodo ipsum sed arcu consectetur fermentum. Orci varius natoque penatibus 
et magnis dis parturient montes, nascetur ridiculus mus. Integer malesuada sollicitudin
 ex, vel porttitor metus tempor at. Morbi tempus, lectus eu fermentum scelerisque, 
 libero dolor efficitur neque, sit amet euismod ex mi id nulla. Proin sit amet congue
   metus. Integer ac aliquam lorem, a tempor lacus. Nulla gravida, massa quis venenatis
     iaculis, nisl libero accumsan nulla, in tincidunt velit odio at urna.''', fecha=timezone.now(), 
     comentarioSimple='''Aliquam orci nibh, bibendum eget viverra id, lacinia non augue. 
     Aliquam viverra sodales arcu, ut placerat sem dictum sed. Suspendisse potenti. Fusce non 
     mollis orci. Aliquam consectetur dictum odio, id ornare elit tincidunt ut. Aliquam ultrices 
     sollicitudin lacus. Curabitur ultrices purus et blandit pharetra.''')

Even3= Evento.objects.create(nombre="21st Work Boys",semana = Sem21,comentario='''Lorem ipsum 
dolor sit amet, consectetur adipiscing elit. 
Sed imperdiet hendrerit odio, vel dignissim mi pretium non. Nam odio nunc, blandit 
non quam eget, fermentum ornare leo. 
Proin consequat tincidunt rhoncus. Aliquam tempus vulputate nisi vitae tincidunt. 
Vestibulum consequat, libero eget tincidunt varius, elit neque ornare nulla,
 quis malesuada magna tortor non tortor. Sed egestas magna porttitor libero 
 tristique, vitae gravida nunc scelerisque. Nullam enim eros, tempus non dapibus 
 vehicula, porttitor et sem. Nulla massa est, rhoncus nec rhoncus at, consectetur sit amet 
 augue. Duis non tempor arcu. Aenean lacinia sem ac maximus consequat. Integer in ultrices quam.
   Quisque sed leo laoreet, tempor risus ac, consequat purus.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames 
ac turpis egestas. Vivamus accumsan ultricies augue, suscipit imperdiet ex ultricies 
eu. Intfermentum. Orci varius natoque penatibus 
et magnis dis parturient montes, nascetur ridiculus mus. Integer malesuada sollicitudin
 ex, vel porttitor metus tempor at. Morbi tempus, lectus eu fermentum scelerisque, 
 libero dolor efficitur neque, sit amet euismod ex mi id nulla. Proin sit amet congue
   metus. Integer ac aliquam lorem, a tempor lacus. Nulla gravida, massa quis venenatis
     iaculis, nisl libero accumsan nulla, in tincidunt velit odio at urna.''', fecha=timezone.now(), 
     comentarioSimple='''Aliquam orci nibh, bibendum eget viverra id, lacinia non augue. 
     Aliquam viverra sodales arcu, ut placerat sem dictum sed. Suspendisse potenti. Fusce non 
     mollis orci. Aliquam consectetur dictum odio, id ornare elit tincidunt ut. Aliquam ultrices 
     sollicitudin lacus. Curabitur ultrices purus et blandit pharetra.''')

Even4= Evento.objects.create(nombre="31th Work Boys",semana = Sem31,comentario='''Lorem ipsum 
dolor sit amet, consectetur adipiscing elit. 
Sed imperdiet hendrerit odio, vel dignissim mi pretium non. Nam odio nunc, blandit 
non quam eget, fermentum ornare leo. 

Pellentesque habitant morbi tristique senectus et netus et malesuada fames 
ac turpis egestas. Vivamus accumsan ultricies augue, suscipit imperdiet ex ultricies 
eu. Integer tincidunt efficitur dignissim. Nulla ultrices nibh tortor, 
vel elementum nibh fermentum eget. Sed quis dictum dui. Maecenas condimentum 
imperdiet interdum. Mauris pretium at risus bibendum commodo. Mauris dolor sem, 
sagittis id odio pretium, viverra vulputate erat. Nam id pulvinar magna, quis euismod 
risus. Sed commodo ipsum sed arcu consectetur fermentum. Orci varius natoque penatibus 
et magnis dis parturient montes, nascetur ridiculus mus. Integer malesuada sollicitudin
 ex, vel porttitor metus tempor at. Morbi tempus, lectus eu fermentum scelerisque, 
 libero dolor efficitur neque, sit amet euismod ex mi id nulla. Proin sit amet congue
   metus. Integer ac aliquam lorem, a tempor lacus. Nulla gravida, massa quis venenatis
     iaculis, nisl libero accumsan nulla, in tincidunt velit odio at urna.''', fecha=timezone.now(), 
     comentarioSimple='''Aliquam orci nibh, bibendum eget viverra id, lacinia non augue. 
     Aliquam viverra sodales arcu, ut placerat sem dictum sed. Suspendisse potenti. Fusce non 
     mollis orci. Aliquam consectetur dictum odio, id ornare elit tincidunt ut. Aliquam ultrices 
     sollicitudin lacus. Curabitur ultrices purus et blandit pharetra.''')

Even5= Evento.objects.create(nombre="2th Work Boys",semana = Sem1,comentario='''Lorem ipsum 
dolor sit amet, consectetur adipiscing elit. 
Sed imperdiet hendrerit odio, vel dignissim mi pretium non. Nam odio nunc, blandit 
non quam eget, fermentum ornare leo. 
Proin consequat tincidunt rhoncus. Aliquam tempus vulputate nisi vitae tincidunt. 
Vestibulum consequat, libero eget tincidunt varius, elit neque ornare nulla,
 quis malesuada magna tortor non tortor. Sed egestas magna porttitor libero 
 tristique, vitae gravida nunc scelerisque. Nullam enim eros, tempus non dapibus 
 vehicula, porttitor et sem. Nulla massa est, rhoncus nec rhoncus at, consectetur sit amet 
 augue. Duis non tempor arcu. Aenean lacinia sem ac maximus consequat. Integer in ultrices quam.
   Quisque sed leo laoreet, tempor risus ac, consequat purus.''', fecha=timezone.now(), 
     comentarioSimple='''Aliquam orci nibh, bibendum eget viverra id, lacinia non augue. 
     Aliquam viverra sodales arcu, ut placerat sem dictum sed. Suspendisse potenti. Fusce non 
     mollis orci. Aliquam consectetur dictum odio, id ornare elit tincidunt ut. Aliquam ultrices 
     sollicitudin lacus. Curabitur ultrices purus et blandit pharetra.''')

Even1.save();Even2.save();Even3.save();Even4.save();Even5.save()

# # # CREAR EJERCICIOS PARA CADA EVENTO (solo 1 por facilidad)

Ejer1 = Ejercicio.objects.create(tipo="ResMult",puntaje=10,evento=Even5)
Ejer2 = Ejercicio.objects.create(tipo="ResUni",puntaje=10,evento=Even5)

Ejer1.save();Ejer2.save()

# # # CREAR OPCIONES PARA LOS EJERCICIOS DEL 2DO EVENTO DE LA SEM 1

Op1_1 = Opciones.objects.create(opcion='correcta',correcta = True, ejercicio=Ejer1)
Op1_2 = Opciones.objects.create(opcion='incorrecta',correcta = False, ejercicio=Ejer1)
Op1_3 = Opciones.objects.create(opcion='correcta',correcta = True, ejercicio=Ejer1)
Op1_4 = Opciones.objects.create(opcion='incorrecta',correcta = False, ejercicio=Ejer1)

Op1_1.save();Op1_2.save();Op1_3.save(),Op1_4.save()

Op1_1 = Opciones.objects.create(opcion='incorrecta',correcta = False, ejercicio=Ejer2)
Op1_2 = Opciones.objects.create(opcion='incorrecta',correcta = False, ejercicio=Ejer2)
Op1_3 = Opciones.objects.create(opcion='correcta',correcta = True, ejercicio=Ejer2)
Op1_4 = Opciones.objects.create(opcion='incorrecta',correcta = False, ejercicio=Ejer2)

Op1_1.save();Op1_2.save();Op1_3.save(),Op1_4.save()

# # # CREAR TEMA DE INVESTIGACION
cont = Contenido.objects.create(tipo='pdf',ubic="/aqui") ####→→→ Necesario guardarlo?
TemInv1 = cont.tema_set.create(nombre='Word Studies')
TemInv2 = cont.tema_set.create(nombre='Physics')
TemInv3 = Tema.objects.create(nombre='Philosophy')

TemInv1.save();TemInv2.save();TemInv3.save()

# # # CREAR USUARIO

UsProf = Usuario.objects.create(nombre_usuario='Victor Parra',nickname='ElProfe',contraseña='Victor',profesor=True)
Us1 = Usuario.objects.create(nombre_usuario="A",nickname="A",contraseña="A",profesor=False,temaInv=TemInv1,curso=curso11_2)
Us2 = Usuario.objects.create(nombre_usuario="B",nickname="B",contraseña="B",profesor=False,temaInv=TemInv2,curso=curso10_4)

UsProf.save();Us1.save(),Us2.save()

# # # CREAR CONTENIDO

Con1 = Contenido.objects.create(tipo='video',ubic='src/Guide-Extended-Essay-1.pdf')
Con2 = Contenido.objects.create(tipo='pdf',ubic='src/Introduction_to_IB_TheExtendedEssay.mp4')



