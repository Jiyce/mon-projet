import cherrypy
import os
import psycopg2

class MonSiteWeb(object):
    
   # Connexion à la base de données
    def connexion_db(self):
        return psycopg2.connect(os.environ.get("DATABASE_URL"))
    
    
    # Page d'accueil    
    @cherrypy.expose
    def index(self):
        return """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
        <title>APPLICATION</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #0a45b3, #0d83f1);
                margin: 0;
                padding: 0;
                /* Centrage de la page d'accueil */
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .container {
                max-width: 600px;
                margin: 50px auto;
                background-color: #fff;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
            }

            /* Styles pour les titres */
            h1 {
                text-align: center;
                color: #0c55df;
                font-size: 32px;
                margin-bottom: 20px;
                
            }
            a {
                display: inline-block;
                justify-content: center;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #0c6ce9;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                transition: color 0.5s ease-in-out;
            }
            
            button {
                background-color: #0c6ce9;
                font-size: 18px;
                padding: 10px 20px;
                border-radius: 6px;
                cursor: pointer;
            }

            /*Styles pour les paragraphes */
            p {
                text-align: center;
                word-spacing: 6px;
                color: #444;
                line-height: 1.6;
                font-size: 18px;
            }
        </style>
            
        </head>
        
        <body>
            <div class="container">
                <h1><i><b>SANTE SEXUELLE ET REPRODUCTIVE</b></i></h1>
                <p><strong>
                 Cette application a pour but d'évaluer les connaissances, les pratiques et les obstacles à l'accès
                  au soins en santé sexuelle et reproductive chez les jeunes afin d'orienter une campagne de prévention
                  locale. Les données collectées sont anonymes et serviront à des fins éducatives.
                </strong></p>
        
                <a href="/questionnaire1">
                    <button>Commencer le questionnaire 👈️ </button>
                </a>
                
                <a href="/stats">
                    <button>Voir les statistiques 📊️</button>
                </a>
            </div>
        </body>
        </html>    
        """
        
        # Questionnaire de santé sexuelle et reproductive  
         
    @cherrypy.expose
    def questionnaire1(self):
        return '''
        <html>
        <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #0a45b3, #0d83f1);
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 600px;
                margin: 50px auto;
                background-color: #fff;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
            }

            /* Styles pour les titres */
            h1 {
                text-align: center;
                color: #0c55df;
                font-size: 32px;
                margin-bottom: 20px;
                
            }

            /*Styles pour les paragraphes */
            p {
                text-align: center;
                color: #555;
                font-size: 18px;
            }

            label {
                font-weight: bold;
            }
            
            ul {
                list-style: none;
                padding: 0;
            }

            /* Styles pour les champs de formulaire */
            input, select, textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0 20px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }   

            input[type="radio"] {
                width: auto;
                margin-right: 10px;
            }

            /* Styles pour les boutons */
            button, input[type="submit"] {
                background-color: #0c6ce9;
                color: white;
                padding: 10px 20px;
                border: none;
                width: 100%;
                border-radius: 4px;
                cursor: pointer;
            }

            button:hover, input[type="submit"]:hover {
                background-color: #00c6ff;
            }
        </style>
                        
        </head>
        
        <body>
        <div class="container">
        
        <h1><i>QUESTIONNAIRE DE SANTÉ SEXUELLE ET REPRODUCTIVE</i></h1>
        <p>Veuillez répondre aux questions suivantes :</p>
        
        <form method="post" action="/questionnaire2">
        
        <h2><i>Page 1 du questionnaire</i></h2>
        
        <ul>
        <li>
        <label>1. Age : </label>
            <select name="age" required>
                <option value="15-19">15-19 ans</option>
                <option value="20-25">20-25 ans</option>
                <option value="25-30">25-30 ans</option>
                <option value="30+">30 ans et plus</option>
            </select><br><br>
        </li>
        
        <li>
        <label>2. Sexe 🚻️: </label>
            <select name="sexe" required>
                <option value="Homme">Homme♂️</option>
                <option value="Femme">Femme♀️</option>
            </select><br><br>
        </li>
        
        <li>    
        <label>3. Avez-vous déjà participez à une campagne de sensibilisation sur la santé sexuelle et reproductive ?</label>
        <input type="radio" id="oui1" name="sensibilisation" value="Oui" >Oui
        <input type="radio" id="non1" name="sensibilisation" value="Non" >Non<br><br>
        </li>
        
        <li>
        <label>4. Etes_vous sexuellement actif ?</label>
        <input type="radio" id="oui2" name="dernier_rapport" value="Oui" required>
        <label for="oui2">Oui</label>
        <input type="radio" id="non2" name="dernier_rapport" value="Non" required>
        <label for="non2">Non</label><br><br>
        </li>
        
        <li>
        <label>5. Age du premier rapport sexuel :</label>
            <input type="number" name="age_premier_rapport" min="10" max="50" required><br><br>
        </li>
        
        <li>
        <label>6. Combien de partenaires sexuels avez-vous eu au cours de votre vie ? :</label>
            <select name="partenaires" required>
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2-5">2-5</option>
                <option value="5+">5 et plus</option>
            </select><br><br>
        </li>
        
        <li>
        <label>7. Quelle méthode de contraception utilisez-vous ?</label>
            <select name="contraception" required>
                <option value="Aucune">Aucune</option>
                <option value="Préservatif">Préservatif</option>
                <option value="Pilule">Pilule</option>
                <option value="Stérilet">Stérilet</option>
                <option value="Autre">Autre</option>
            </select><br><br>
        </li>
        
        <li>
        <label>8. Avez-vous déjà été testé pour les infections sexuellement transmissibles (ist) ?</label>
            <input type="radio" id="oui3" name="ist" value="Oui" required>
            <label for="oui3">Oui</label>
            <input type="radio" id="non3" name="ist" value="Non" required>
            <label for="non3">Non</label><br><br> 
        </li>
            
        <li>
            <label>9. Le préservatif est-il efficace pour prévenir les grossesses et les ist ?</label>
            <input type="radio" id="oui4" name="preservatif" value="Oui" required>
            <label for="oui4">Oui</label><br>
            <input type="radio" id="non4" name="preservatif" value="Non" required>
            <label for="non4">Non</label><br><br>
        </li>
        
        <li>
        <label>10. Quels sont les risques associés à une activité sexuelle non protégée ?</label>
            <textarea name="risques" rows="4" cols="50" placeholder="Veuillez décrire les risques..." required></textarea><br><br>
        </li>
        
        </ul>
        
        <input type= 'submit' value='Suivant'>
        </form>
        </body>
        </html>
        '''
        
    @cherrypy.expose
    def questionnaire2(self, **data):
        hidden_inputs = ''.join([f'<input type="hidden" name="{key}" value="{value}">' for key, value in data.items()])
        return f'''
        <html>
        <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #0a45b3, #0d83f1);
                margin: 0;
                padding: 20px;
            }}

            .container {{
                max-width: 600px;
                margin: 50px auto;
                background-color: #fff;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
            }}

            /* Styles pour les titres */
            h1 {{
                text-align: center;
                color: #0c55df;
                font-size: 32px;
                
            }}

            /*Styles pour les paragraphes */
            p {{
                text-align: center;
                color: #555;
                font-size: 18px;
            }}

            label {{
                font-weight: bold;
            }}
            
            ul {{
                list-style: none;
                padding: 0;
            }}

            /* Styles pour les champs de formulaire */
            input, select, textarea {{
                width: 100%;
                padding: 10px;
                margin: 10px 0 20px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }}  

            input[type="radio"] {{
                width: auto;
                margin-right: 10px;
            }}

            /* Styles pour les boutons */
            button, input[type="submit"] {{
                background-color: #0c6ce9;
                color: white;
                padding: 10px 20px;
                border: none;
                width: 100%;
                border-radius: 4px;
                cursor: pointer;
            }}

            button:hover, input[type="submit"]:hover {{
                background-color: #00c6ff;
            }}
        </style>
        
        </head>
        <body>
        <div class="container">
        <h2> Page 2 du questionnaire</h2>
        
        <form method="post" action="/submit">
        {hidden_inputs}
        
        <ul>
        
        <li>
        <label>11. Selon vous qui sont les plus exposées au phénomène de la sexualité précoce ? Justifiez votre réponse.</label>
            <textarea name="sexualite_precoce" rows="4" cols="50" placeholder="Veuillez décrire..." required></textarea><br><br>
        </li>
        
        <li>
        <label>12. Quels sont les facteurs qui peuvent influencer les comportements sexuels à risque chez les jeunes ?</label>
            <textarea name="facteurs" rows="4" cols="50" placeholder="Veuillez décrire les facteurs..." required></textarea><br><br>
        </li>
        
        <li>
        <label>13. Quels sont les moyens de prévention que vous connaissez pour éviter les infections sexuellement transmissibles et les grossesses non désirées ?</label>
            <textarea name="prevention" rows="4" cols="50" placeholder="Veuillez décrire les moyens de prévention..." required></textarea><br><br>
        </li>
        
        <li>
        <label>14. Quelles sont les différentes maladies sexuellement transmissibles (mst) que vous connaissez ?</label>
            <textarea name="mst" rows="4" cols="50" placeholder="Veuillez lister les maladies..." required></textarea><br><br>
        </li>
        
        <li>
        <label>15. Avez-vous déjà consulter un professionnel de santé?</label>
           <input type="radio" id="oui5" name="acces_sante" value="Oui" required>
            <label for="oui5">Oui</label>
            <input type="radio" id="non5" name="acces_sante" value="Non" required>
            <label for="non5">Non</label><br><br>
        </li>
        
        <li>
        <label>16. A quelle fréquence consultez-vous un professionnel de santé ?</label>
            <select name="frequence_sante" required>
                <option value="Jamais">Jamais</option>
                <option value="Rarement">Rarement</option>
                <option value="Régulièrement">Régulièrement</option>
            </select><br><br>
        </li>
        
        <li>
        <label>17. Quelles difficultés rencontrez-vous pour accéder aux services de santé  ?</label>
            <textarea name="difficultes" rows="4" cols="50" placeholder="Veuillez décrire les difficultés..." required></textarea><br><br>
        </li>

        <li>
        <label>18. Utilisez-vous toujours une protection lors de vos rapports sexuels ?</label>
            <input type="radio" id="oui6" name="protection" value="Oui" required>
            <label for="oui6">Oui</label>
            <input type="radio" id="non6" name="protection" value="Non" required>
            <label for="non6">Non</label><br><br>
        </li>
        
        <li>
        <label>19. Pensez-vous que l'éducation sexuelle est suffisante pour les jeunes ?</label>
            <input type="radio" id="oui7" name="education" value="Oui" required>
            <label for="oui7">Oui</label>
            <input type="radio" id="non7" name="education" value="Non" required>
            <label for="non7">Non</label><br><br>
        </li>
        
        
        <li>
         <label>20. Comment amélioreriez-vous l'accès à l'éducation sexuelle et aux services de santé reproductive pour les jeunes ?</label>
            <textarea name="amelioration" rows="4" cols="50" placeholder="Vos suggestions..." required></textarea><br><br>
        </li>
        </ul>
            
        <input type="submit" value="Soumettre">         
        </form>
        
        </div>
        </body>
        </html>
    '''
    # Traitement des données du formulaire
    
    @cherrypy.expose
    def submit(self, **data):
        age = data.get('age')
        sexe = data.get('sexe')
        sensibilisation = data.get('sensibilisation')
        dernier_rapport = data.get('dernier_rapport')
        contraception = data.get('contraception')
        mst = data.get('mst')
        amelioration = data.get('amelioration')
        ist = data.get('ist')
        preservatif = data.get('preservatif')   
        partenaires = data.get('partenaires')
        age_premier_rapport = data.get('age_premier_rapport')
        acces_sante = data.get('acces_sante')
        protection = data.get('protection')
        education = data.get('education')
        difficultes = data.get('difficultes')
        frequence_sante = data.get('frequence_sante')
        prevention = data.get('prevention')
        sexualite_precoce = data.get('sexualite_precoce')
        facteurs = data.get('facteurs')
        risques = data.get('risques')
        
        if not all([age, sexe, sensibilisation, dernier_rapport, contraception, mst, amelioration, ist, preservatif, partenaires,
                    age_premier_rapport, acces_sante, protection, education, difficultes, frequence_sante,
                    prevention, sexualite_precoce, facteurs, risques]):
            return "<h1>Erreur : Tous les champs sont obligatoires. Veuillez remplir le formulaire correctement.</h1><a href='/questionnaire1'>Retour au questionnaire</a>"
        
        conn = self.connexion_db()
        cursor = conn.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS reponses (
                       id SERIAL PRIMARY KEY,
                       age VARCHAR(20),
                       sexe VARCHAR(20),
                       sensibilisation VARCHAR(10),
                       dernier_rapport VARCHAR(10),
                       contraception VARCHAR(20),
                       mst TEXT,
                       amelioration TEXT,
                       ist VARCHAR(10),
                       prevention TEXT,
                       sexualite_precoce TEXT,
                       facteurs TEXT,
                       risques TEXT,
                       preservatif VARCHAR(10), 
                       partenaires VARCHAR(20),
                        age_premier_rapport INTEGER,
                         acces_sante VARCHAR(10),
                        protection VARCHAR(10),
                        education VARCHAR(10),
                        difficultes TEXT,
                        frequence_sante VARCHAR(20)
                       )""")
        cursor.execute("""INSERT INTO reponses (age, sexe, sensibilisation,dernier_rapport,contraception,mst, amelioration, ist, preservatif, partenaires, 
                       age_premier_rapport, acces_sante, protection, education, difficultes, 
                       frequence_sante, prevention, sexualite_precoce, facteurs, risques) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                       (age, sexe, sensibilisation,dernier_rapport,contraception,mst, amelioration, ist, preservatif, 
                        partenaires, age_premier_rapport, acces_sante, protection, education, difficultes, frequence_sante, prevention, sexualite_precoce, facteurs, risques))
        conn.commit()
        conn.close()
        
        return """
    
        <html>
        <head>
            <style>
                body {
                    font-family: Arial;
                    background: linear-gradient(to right, #0a45b3, #0d83f1);
                    display: flex;
                    justify-content:center;
                    align-items: center; 
                    margin: 0; }
                .card {
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    text-align: center;
                    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                    max-width: 500px; }
                h1 {
                    color: #0c55df;
                    font-size: 2.5em; 
                }
                .btn { 
                   display: inline-block;
                   margin: 10px;
                   padding: 12px 24px; 
                   background: #0c6ce9;
                   color: white;
                   text-decoration: none;
                   border-radius: 6px;
                   transition: 0.3s;
                }
                .btn:hover { 
                    background: #00c6ff;
                    transform: translateY(-2px);
                }
                .icon { 
                   font-size: 50px; 
                }
                
            </style>
        </head>
        <body>
            <div class="card">
                <div class="icon">✅</div>
    
    
                <h1>Merci pour votre participation 😁️!</h1>
                <a href="/stats">Voir les statistiques des participants📊️</a><br><br>
                <a href="/">Retour à l'accueil🎲️</a>
            </div>
        </body>
        </html>
         """
    
    @cherrypy.expose
    def stats(self):
        conn = self.connexion_db()
        cursor = conn.cursor()
        
        #Nombre total de participants
        cursor.execute("SELECT COUNT(*) FROM  reponses")
        total = cursor.fetchone()[0]
        
        #Repartition par sexe
        cursor.execute("""
                       SELECT sexe,  COUNT(*) 
                       FROM reponses
                       GROUP BY sexe
                          """)
        repartition_sexe = cursor.fetchall()
        
        questions_textuelles = ['risques', 'sexualite_precoce', 'facteurs', 'prevention', 'mst', 'amelioration', 'difficultes']
        stats_textuelles = {}
        
        for colonne in questions_textuelles:
            cursor.execute(f"""
                           SELECT sexe, LOWER(TRIM({colonne})) AS reponse, COUNT(*) as nb
                           FROM reponses
                           WHERE {colonne} IS NOT NULL AND TRIM({colonne}) != ''
                           GROUP BY sexe, reponse
                           HAVING COUNT(*) > 1
                           ORDER BY sexe,nb DESC
                        """)
            reponses = cursor.fetchall()
            stats_textuelles[colonne] = reponses
        conn.close()
        
        html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial;
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    text-align: center;
                    padding: 50px;
                }}

                .container {{
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    width: 50%;
                    margin: auto;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);
                }}

                h1 {{
                    color: #10037e;
                }}

                ul {{
                    list-style: none;
                    padding: 0;
                }}

                li {{
                    font-size: 18px;
                    margin: 10px 0;
                }}

                a {{
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    background: #10037e;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 5px;
                }}

                a:hover {{
                    background: #00c6ff;
                }}
            </style>
        </head>
        
        <body>
        <div class="container">
            <h1>Statistiques des participants</h1>
        
            <p><strong>Total de participants : </strong> {total}</p>
            
            <h2><i>Repartition par sexe :</i></h2>
            <ul>
            """
            
        for sexe, count in repartition_sexe:
                pourcentage = (count / total) * 100 if total > 0 else 0
                html += f"<li>{sexe} : {count} ({pourcentage:.2f}%)</li>"
        html += "</ul>"
                
        html += "<h2><i>Statistiques des réponses textuelles :</i></h2>"
        for question, reponses in stats_textuelles.items():
            html += f"<h3>{question}</h3><ul>"
            
            data_par_sexe = {}
            for sexe, reponse, nb in reponses:
                 if sexe not in data_par_sexe:
                    data_par_sexe[sexe] = []
                    data_par_sexe[sexe].append((reponse, nb))
            
            for sexe, liste in data_par_sexe.items():
                html += f"<strong><h4>{sexe} :</h4></strong><ul>"
                for reponse, nb in liste:
                    html += f"<li>{reponse} ({nb} réponses)</li>"
                html += "</ul>"
        html += """
             <a href="/">Retour à l'accueil</a>
        </div>
        </body>
        </html>
            """
        
            
        return html
     
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))

    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': int(os.environ.get('PORT', 8081))
                            })
    cherrypy.quickstart(MonSiteWeb(), '/', config={
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(current_dir, 'static')
        }
    })
    
