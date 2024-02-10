y='Updations Done Successfully!!!'
x='appdate'
w='speciality'
v='password'
u='loginpage3.html'
t='loginpage2.html'
s='loginpage1.html'
r=print
m='doctorlogin.html'
l='Please enter correct credentials...'
k='pass'
j='%Y-%m-%d'
i=any
f='patientlogin.html'
e='address'
d='dob'
c='lastname'
b='firstname'
a=True
W='patnum'
V='-'
U=False
T='SELECT * FROM patients'
S='phn'
R='SELECT * FROM doctors'
P='adminlogin.html'
O='GET'
N='docid'
I='POST'
H='home.html'
E=len
C=str
from datetime import datetime as n
import sqlite3 as z
from datetime import date
from flask import Flask,request as B,render_template as F
G=Flask(__name__)
D=z.connect('database/lifecare.db',check_same_thread=U)
A=D.cursor()
A.execute('CREATE TABLE IF NOT EXISTS doctors(\n            first_name text,\n            last_name text,\n            dob date,\n            phone_number integer,\n            address integer text,\n            doc_id integer text,\n            password integer text,\n            speciality text,\n            status integer\n            )')
A.execute('CREATE TABLE IF NOT EXISTS patients(\n            first_name text,\n            last_name text,\n            dob date,\n            phone_number integer,\n            password integer text,\n            address integer text,\n            status integer\n            )')
A.execute('CREATE TABLE IF NOT EXISTS superusercreds(\n            username integer text,\n            password integer text\n            )')
A.execute('CREATE TABLE IF NOT EXISTS doctorappointmentrequests(\n            docid integer text,\n            patientname integer text,\n            patientnum integer text,\n            appointmentdate date\n            )')
A.execute('CREATE TABLE IF NOT EXISTS doctorappointments(\n            docid integer text,\n            patientname integer text,\n            patientnum integer text,\n            appointmentdate date\n            )')
A.execute('SELECT * from superusercreds')
D.commit()
A0=A.fetchall()
if not A0:A.execute("INSERT INTO superusercreds VALUES ('admin','admin')");D.commit()
def o():A=n.now().strftime(j);return A
def Q(x):return x.isalpha()
def A6(x):return x.isdigit()
def p(x):
	A,B,C=U,U,U
	if E(x)<8:return U
	if i((A.isalpha()for A in x)):A=a
	if i((A.isdigit()for A in x)):B=a
	if i((A in x for A in['@','$','!'])):C=a
	return A and B and C
def q(x):return E(x)==10
def X():A.execute(f"SELECT * FROM doctorappointments");D.commit();B=A.fetchall();C=E(B);return B,C
def A1(phn):
	A.execute(f"SELECT * FROM patients");D.commit();E=A.fetchall()
	for B in E:
		if C(B[3])==C(phn):return B
def A2(docid):
	A.execute(f"SELECT * FROM doctors");D.commit();E=A.fetchall()
	for B in E:
		if C(B[5])==C(docid):return B
def g(docid):
	A.execute(f"SELECT * FROM doctorappointments");D.commit();G=A.fetchall();B=[]
	for F in G:
		if C(F[0])==C(docid):B.append(F)
	H=E(B);return B,H
def h(docid):
	A.execute(f"SELECT * FROM doctorappointmentrequests");D.commit();B=A.fetchall();F=[]
	for G in B:
		if C(G[0])==C(docid):F.append(G)
	H=E(F);return B,H
def J():
	A.execute(T);D.commit();F=A.fetchall();B=[]
	for E in F:
		if C(E[-1])=='0':B.append(E)
	return B
def K():
	A.execute(R);D.commit();F=A.fetchall();B=[]
	for E in F:
		if C(E[-1])=='0':B.append(E)
	return B
def L():
	A.execute(T);D.commit();F=A.fetchall();B=[]
	for E in F:
		if C(E[-1])=='1':B.append(E)
	return B
def M():
	A.execute(R);D.commit();F=A.fetchall();B=[]
	for E in F:
		if C(E[-1])=='1':B.append(E)
	return B
def Y():
	A.execute(R);D.commit();G=A.fetchall();F=[]
	for B in G:F.append(C(B[0])+' '+C(B[1])+V+C(B[5])+V+C(B[7]))
	H=E(F);return F,H
def Z(docid):
	A.execute(R);D.commit();E=A.fetchall()
	for B in E:
		if C(B[5])==C(docid):return B[0]+V+B[1]
def A3(patnum):
	A.execute(T);D.commit();E=A.fetchall()
	for B in E:
		if C(B[3])==C(patnum):return B[0]+' '+B[1]
	else:return-1
def A4():
	A.execute(R);D.commit();E=A.fetchall();B=[]
	for F in E:B.append(C(F[5]))
	return B
def A5():
	A.execute(T);D.commit();E=A.fetchall();B=[]
	for F in E:B.append(C(F[3]))
	return B
@G.route('/')
def A7():return F(H)
@G.route('/patreg')
def A8():return F('patientregistration.html')
@G.route('/docreg')
def A9():return F('doctorregistration.html')
@G.route('/loginpage1')
def AA():return F(s)
@G.route('/loginpage2')
def AB():return F(t)
@G.route('/loginpage3')
def AC():return F(u)
@G.route('/addpatient',methods=[I])
def AD():
	J=B.form[v];E=B.form[b];G=B.form[c];K=B.form[d];I=B.form[S];L=B.form[e];r(E,G,Q(E),Q(G))
	if(not Q(E))|(not Q(G)):return F(H,mess=f"First Name and Last Name can only contain alphabets.")
	if not p(J):return F(H,mess=f"Password should be of length 8 and should contain alphabets, numbers and special characters ('@','$','!').")
	if not q(I):return F(H,mess=f"Phone number should be of length 10.")
	if C(I)in A5():return F(H,mess=f"Patient with mobile number {I} already exists.")
	A.execute(f"INSERT INTO patients VALUES ('{E}','{G}','{K}','{I}','{J}','{L}',0)");D.commit();return F(H,mess=f"Registration Request sent to Super Admin for Patient {E}.")
@G.route('/adddoctor',methods=[O,I])
def AE():
	I=B.form[v];E=B.form[b];J=B.form[c];M=B.form[d];K=B.form[S];O=B.form[e];G=B.form[N];L=B.form[w]
	if not Q(E)and not Q(J):return F(H,mess=f"First Name and Last Name can only contain alphabets.")
	if not Q(L):return F(H,mess=f"Doctor Speciality can only contain alphabets.")
	if not p(I):return F(H,mess=f"Password should be of length 8 and should contain alphabets, numbers and special characters ('@','$','!').")
	if not q(K):return F(H,mess=f"Phone number should be of length 10.")
	if C(G)in A4():return F(H,mess=f"Doctor with Doc ID {G} already exists.")
	A.execute(f"INSERT INTO doctors VALUES ('{E}','{J}','{M}','{K}','{O}','{G}','{I}','{L}',0)");D.commit();return F(H,mess=f"Registration Request sent to Super Admin for Doctor {E}.")
@G.route('/patientlogin',methods=[O,I])
def AF():
	G=B.form[S];J=B.form[k];A.execute(T);D.commit();K=A.fetchall()
	for E in K:
		if C(E[3])==C(G)and C(E[4])==C(J):
			H,L=X();M,N=Y();I=[]
			for E in H:I.append(Z(E[0]))
			return F(f,docsandapps=H,docnames=I,docname_docid=M,l=L,l2=N,patname=E[0],phn=G)
	else:return F(s,err=l)
@G.route('/doctorlogin',methods=[O,I])
def AG():
	E=B.form[N];H=B.form[k];A.execute(R);D.commit();I=A.fetchall()
	for G in I:
		if C(G[5])==C(E)and C(G[6])==C(H):J,K=h(E);L,M=g(E);return F(m,appointment_requests_for_this_doctor=J,fix_appointment_for_this_doctor=L,l1=K,l2=M,docname=G[0],docid=E)
	else:return F(t,err=l)
@G.route('/adminlogin',methods=[O,I])
def AH():
	Q=B.form['username'];R=B.form[k];A.execute('SELECT * FROM superusercreds');D.commit();S=A.fetchall()
	for G in S:
		if C(G[0])==C(Q)and C(G[1])==C(R):H=J();I=K();N=L();O=M();T=E(H);U=E(I);V=E(N);W=E(O);return F(P,patient_reg_requests=H,doctor_reg_requests=I,registered_patients=N,registered_doctors=O,l1=T,l2=U,l3=V,l4=W)
	else:return F(u,err=l)
@G.route('/deletepatient',methods=[O,I])
def AI():O=B.values[W];A.execute(f"DELETE FROM patients WHERE phone_number='{C(O)}' ");D.commit();G=J();H=K();I=L();N=M();Q=E(G);R=E(H);S=E(I);T=E(N);return F(P,patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=N,l1=Q,l2=R,l3=S,l4=T)
@G.route('/deletedoctor',methods=[O,I])
def AJ():Q=B.values[N];A.execute(f"DELETE FROM doctors WHERE doc_id='{C(Q)}' ");D.commit();G=J();H=K();I=L();O=M();R=E(G);S=E(H);T=E(I);U=E(O);return F(P,patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=O,l1=R,l2=S,l3=T,l4=U)
@G.route('/makeappointment',methods=[O,I])
def AK():
	L=B.args[S];M=B.form[x];N=B.form['whichdoctor'];Q=N.split(V)[0];P=N.split(V)[1];G=A3(L);O=n.strptime(M,j).strftime(j);r(O,o())
	if O>o():
		if G!=-1:
			A.execute(f"INSERT INTO doctorappointmentrequests VALUES ('{P}','{G}','{L}','{M}')");D.commit();C,H=X();I,J=Y();E=[]
			for K in C:E.append(Z(K[0]))
			return F(f,mess=f"Appointment Request sent to doctor.",docnames=E,docsandapps=C,docname_docid=I,l=H,l2=J,patname=G)
		else:
			C,H=X();I,J=Y();E=[]
			for K in C:E.append(Z(K[0]))
			return F(f,mess=f"No user with such contact number.",docnames=E,docsandapps=C,docname_docid=I,l=H,l2=J,patname=G)
	else:
		C,H=X();I,J=Y();E=[]
		for K in C:E.append(Z(K[0]))
		return F(f,mess=f"Please select a date after today.",docnames=E,docsandapps=C,docname_docid=I,l=H,l2=J,patname=G)
@G.route('/approvedoctor')
def AL():
	V=B.values[N];A.execute(R);D.commit();W=A.fetchall()
	for X in W:
		if C(X[5])==C(V):A.execute(f"UPDATE doctors SET status=1 WHERE doc_id={C(V)}");D.commit();G=J();H=K();I=L();O=M();Q=E(G);S=E(H);T=E(I);U=E(O);return F(P,mess=f"Doctor Approved successfully!!!",patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=O,l1=Q,l2=S,l3=T,l4=U)
	else:G=J();H=K();I=L();O=M();Q=E(G);S=E(H);T=E(I);U=E(O);return F(P,mess=f"Doctor Not Approved...",patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=O,l1=Q,l2=S,l3=T,l4=U)
@G.route('/approvepatient')
def AM():
	U=B.values[W];A.execute(T);D.commit();V=A.fetchall()
	for X in V:
		if C(X[3])==C(U):A.execute(f"UPDATE patients SET status=1 WHERE phone_number={C(U)}");D.commit();G=J();H=K();I=L();N=M();O=E(G);Q=E(H);R=E(I);S=E(N);return F(P,mess=f"Patient Approved successfully!!!",patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=N,l1=O,l2=Q,l3=R,l4=S)
	else:G=J();H=K();I=L();N=M();O=E(G);Q=E(H);R=E(I);S=E(N);return F(P,mess=f"Patient Not Approved...",patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=N,l1=O,l2=Q,l3=R,l4=S)
@G.route('/doctorapproveappointment')
def AN():E=B.values[N];G=B.values[W];H=B.values['patname'];I=B.values[x];A.execute(f"INSERT INTO doctorappointments VALUES ('{E}','{H}','{G}','{I}')");D.commit();A.execute(f"DELETE FROM doctorappointmentrequests WHERE patientnum='{C(G)}'");D.commit();J,K=h(E);L,M=g(E);return F(m,appointment_requests_for_this_doctor=J,fix_appointment_for_this_doctor=L,l1=K,l2=M,docid=E)
@G.route('/doctordeleteappointment')
def AO():E=B.values[N];G=B.values[W];A.execute(f"DELETE FROM doctorappointmentrequests WHERE patientnum='{C(G)}'");D.commit();H,I=h(E);J,K=g(E);return F(m,appointment_requests_for_this_doctor=H,fix_appointment_for_this_doctor=J,l1=I,l2=K,docid=E)
@G.route('/deletedoctorrequest')
def AP():Q=B.values[N];A.execute(f"DELETE FROM doctors WHERE doc_id='{C(Q)}'");D.commit();G=J();H=K();I=L();O=M();R=E(G);S=E(H);T=E(I);U=E(O);return F(P,patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=O,l1=R,l2=S,l3=T,l4=U)
@G.route('/deletepatientrequest')
def AQ():O=B.values[W];A.execute(f"DELETE FROM patients WHERE phone_number='{C(O)}'");D.commit();G=J();H=K();I=L();N=M();Q=E(G);R=E(H);S=E(I);T=E(N);return F(P,patient_reg_requests=G,doctor_reg_requests=H,registered_patients=I,registered_doctors=N,l1=Q,l2=R,l3=S,l4=T)
@G.route('/updatepatient')
def AR():A=B.args[S];C,D,E,A,G,H,I=A1(A);return F('updatepatient.html',fn=C,ln=D,dob=E,phn=A,passw=G,add=H,status=I)
@G.route('/updatedoctor')
def AS():A=B.args[N];C,D,E,G,H,A,I,J,K=A2(A);return F('updatedoctor.html',fn=C,ln=D,dob=E,phn=G,passw=I,add=H,status=K,spec=J,docid=A)
@G.route('/makedoctorupdates',methods=[O,I])
def AT():E=B.form[b];G=B.form[c];I=B.form[d];J=B.form[S];K=B.form[e];C=B.args[N];L=B.form[w];A.execute('UPDATE doctors SET first_name=(?) WHERE doc_id=(?)',(E,C));D.commit();A.execute('UPDATE doctors SET last_name=(?) WHERE doc_id=(?)',(G,C));D.commit();A.execute('UPDATE doctors SET dob=(?) WHERE doc_id=(?)',(I,C));D.commit();A.execute('UPDATE doctors SET phone_number=(?) WHERE doc_id=(?)',(J,C));D.commit();A.execute('UPDATE doctors SET address=(?) WHERE doc_id=(?)',(K,C));D.commit();A.execute('UPDATE doctors SET speciality=(?) WHERE doc_id=(?)',(L,C));D.commit();return F(H,mess=y)
@G.route('/makepatientupdates',methods=[O,I])
def AU():E=B.form[b];G=B.form[c];I=B.form[d];C=B.args[S];J=B.form[e];A.execute('UPDATE patients SET first_name=(?) WHERE phone_number=(?)',(E,C));D.commit();A.execute('UPDATE patients SET last_name=(?) WHERE phone_number=(?)',(G,C));D.commit();A.execute('UPDATE patients SET dob=(?) WHERE phone_number=(?)',(I,C));D.commit();A.execute('UPDATE patients SET address=(?) WHERE phone_number=(?)',(J,C));D.commit();return F(H,mess=y)
if __name__=='__main__':G.run(debug=a)