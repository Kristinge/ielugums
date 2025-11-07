from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'jūsu_parole'  # Mainiet uz drošu atslēgu

# Atļautie vārdi sistēmā
ATLAUTIE_VARDI = ["Jānis", "Sergejs", "Inga", "Vladislavs", "Intars", "ievars", "santa", "edgars"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nakama_lapa')
def nakama_lapa():
    # Pārbauda, vai lietotājs ir ielogojies
    if 'lietotajs' not in session:
        return redirect(url_for('index'))
    return render_template('nakama_lapa.html', lietotajs=session['lietotajs'])

@app.route('/parbaudit_vardu', methods=['POST'])
def parbaudit_vardu():
    vards = request.form.get('vards', '').strip().lower()
    
    if not vards:
        return {"success": False, "message": "Lūdzu, ievadi savu vārdu!"}
    
    if vards in ATLAUTIE_VARDI:
        session['lietotajs'] = vards
        return {"success": True, "message": f"Pieeja atļauta! Sveiks, {vards.capitalize()}!"}
    else:
        return {"success": False, "message": "Atvaino, tavs vārds nav sistēmā. Pieeja liegta."}

@app.route('/logout')
def logout():
    session.pop('lietotajs', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
