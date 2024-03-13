from flask import Flask, render_template, request, jsonify
import string

app = Flask(__name__)

def analyze_password(password):
    analysis = {
        'has_numbers': any(char.isdigit() for char in password),
        'has_lowercase': any(char.islower() for char in password),
        'has_uppercase': any(char.isupper() for char in password),
        'has_symbols': any(char in string.punctuation for char in password)
    }
    return analysis

def brute_force_time_estimate(password):
    
    possible_characters = 0
    
    analysis = analyze_password(password)
    if analysis['has_numbers']:
        possible_characters += 10  
    if analysis['has_lowercase']:
        possible_characters += 26  
    if analysis['has_uppercase']:
        possible_characters += 26  
    if analysis['has_symbols']:
        possible_characters += len(string.punctuation) 
    
    password_length = len(password)
    
    total_combinations = possible_characters ** password_length
    
    attempts_per_second = 2.07 * 10**9
    
    time_to_exhaust_seconds = total_combinations / attempts_per_second
    
    seconds = time_to_exhaust_seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    
    return f"{int(years)} years, {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    result = brute_force_time_estimate(password)
    return result

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
