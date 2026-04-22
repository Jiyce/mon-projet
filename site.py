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
                height: 100vh;
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
                
            }

            /*Styles pour les paragraphes */
            p {
                text-align: center;
                color: #555;
                font-size: 18px;
            }
        </style>
            
        </head>
        
        <body>
            <div class="container">
                <h1><i>SANTE SEXUELLE ET REPRODUCTIVE</i></h1>
                <p> 
                 Cette application a pour but d'évaluer les connaissances, les pratiques et les obstacles à l'accès
                  au soins en santé sexuelle et reproductive chez les jeunes afin d'orienter une campagne de prévention
                  locale. Les données collectées sont anonymes et serviront à des fins éducatives.
                </p>
        
                <a href="questionnaire">
                    <button>Commencer le questionnaire 👈️ </button>
                </a>
            </div>
        </body>
        </html>    
        """
        
        # Questionnaire de santé sexuelle et reproductive  
         
    @cherrypy.expose
    def questionnaire(self):
        return '''
        <html>
        <head>
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
                height: 100vh;
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
        
        <form method="post" action="submit">
        
        <ol>
        <li>
        <label>Age : </label>
            <select name="age" required>
                <option value="15-19">15-19 ans</option>
                <option value="20-25">20-25 ans</option>
                <option value="25-30">25-30 ans</option>
                <option value="30+">30 ans et plus</option>
            </select><br><br>
        </li>
        
        <li>
        <label>Sexe 🚻️: </label>
            <select name="sexe" required>
                <option value=" Homme">Homme♂️</option>
                <option value="Femme">Femme♀️</option>
            </select><br><br>
        </li>
        
        </li>    
        <label>Avez-vous déjà participez à une campagne de sensibilisation sur la santé sexuelle et reproductive ?</label>
        <input type="radio" id="oui" name="sensibilisation" value="Oui" >Oui
        <input type="radio" id="non" name="sensibilisation" value="Non" >Non<br><br>
        </li>
        
        <li>
        <label>Etes_vous sexuellement actif ?</label>
        <input type="radio" id="oui" name="dernier_rapport" value="Oui" required>
        <label for="oui">Oui</label>
        <input type="radio" id="non" name="dernier_rapport" value="Non" required>
        <label for="non">Non</label><br><br>
        </li>
        
        <li>
        <label>Age du premier rapport sexuel :</label>
            <input type="number" name="age_premier_rapport" min="10" max="50" required><br><br>
        </li>
        
        <li>
        <label>Combien de partenaires sexuels avez-vous eu au cours de votre vie ? :</label>
            <select name="partenaires" required>
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2-5">2-5</option>
                <option value="5+">5 et plus</option>
            </select><br><br>
        </li>
        
        <li>
        <label>Quelle méthode de contraception utilisez-vous ?</label>
            <select name="contraception" required>
                <option value="Aucune">Aucune</option>
                <option value="Préservatif">Préservatif</option>
                <option value="Pilule">Pilule</option>
                <option value="Stérilet">Stérilet</option>
                <option value="Autre">Autre</option>
            </select><br><br>
        </li>
        
        <li>
        <label>Avez-vous déjà été testé pour les infections sexuellement transmissibles (ist) ?</label>
        <input type="radio" id="oui" name="ist" value="Oui" required>
        <label for="oui">Oui</label>
        <input type="radio" id="non" name="ist" value="Non" required>
        <label for="non">Non</label><br><br> 
        </li>
        
        <li>
        <label>Le préservatif est-il efficace pour prévenir les grossesses et les ist ?</label>
        <input type="radio" id="oui" name="preservatif" value="Oui" required>
        <label for="oui">Oui</label><br>
        <input type="radio" id="non" name="preservatif" value="Non" required>
        <label for="non">Non</label><br><br>
        </li>
        
        <li>
        <label>Quels sont les risques associés à une activité sexuelle non protégée ?</label>
            <textarea name="risques" rows="4" cols="50" placeholder="Veuillez décrire les risques..." required></textarea><br><br>
        </li>
        
        <li>
        <label>Selon vous qui sont les plus exposées au phénomène de la sexualité précoce ? Justifiez votre réponse.</label>
            <textarea name="sexualite_precoce" rows="4" cols="50" placeholder="Veuillez décrire..." required></textarea><br><br>
        </li>
        
        <li>
        <label>Quels sont les facteurs qui peuvent influencer les comportements sexuels à risque chez les jeunes ?</label>
            <textarea name="facteurs" rows="4" cols="50" placeholder="Veuillez décrire les facteurs..." required></textarea><br><br>
        </li>
        
        <li>
        <label>Quels sont les moyens de prévention que vous connaissez pour éviter les infections sexuellement transmissibles et les grossesses non désirées ?</label>
            <textarea name="prevention" rows="4" cols="50" placeholder="Veuillez décrire les moyens de prévention..." required></textarea><br><br>
        </li>
        
        <li>
        <label>Quelles sont les différentes maladies sexuellement transmissibles (mst) que vous connaissez ?</label>
            <textarea name="mst" rows="4" cols="50" placeholder="Veuillez lister les maladies..." required></textarea><br><br>
        </li>
        
        <li>
        <label>Avez-vous déjà consulter un professionnel de santé?</label>
           <input type="radio" id="oui" name="acces_sante" value="Oui" required>
            <label for="oui">Oui</label>
            <input type="radio" id="non" name="acces_sante" value="Non" required>
            <label for="non">Non</label><br><br>
        </li>
        
        <li>
        <label>A quelle fréquence consultez-vous un professionnel de santé ?</label>
            <select name="frequence_sante" required>
                <option value="Jamais">Jamais</option>
                <option value="Rarement">Rarement</option>
                <option value="Régulièrement">Régulièrement</option>
            </select><br><br>
        </li>
        
        <li>
        <label>Quelles difficultés rencontrez-vous pour accéder aux services de santé  ?</label>
            <textarea name="difficultes" rows="4" cols="50" placeholder="Veuillez décrire les difficultés..." required></textarea><br><br>
        </li>

        <li>
        <label>Utilisez-vous toujours une protection lors de vos rapports sexuels ?</label>
            <input type="radio" id="oui" name="protection" value="Oui" required>
            <label for="oui">Oui</label>
            <input type="radio" id="non" name="protection" value="Non" required>
            <label for="non">Non</label><br><br>
        </li>
        
        <li>
        <label>Pensez-vous que l'éducation sexuelle est suffisante pour les jeunes ?</label>
            <input type="radio" id="oui" name="education" value="Oui" required>
            <label for="oui">Oui</label>
            <input type="radio" id="non" name="education" value="Non" required>
            <label for="non">Non</label><br><br>
        </li>
        
        
        <li>
         <label>Comment amélioreriez-vous l'accès à l'éducation sexuelle et aux services de santé reproductive pour les jeunes ?</label>
            <textarea name="amelioration" rows="4" cols="50" placeholder="Vos suggestions..." required></textarea><br><br>
        </li>
        </ol>
            
        <input type="submit" value="Soumettre">         
        </form>
        
        </div>
        </body>
        </html>
        '''
    # Traitement des données du formulaire
    
    @cherrypy.expose
    def submit(self,age, sexe, sensibilisation,dernier_rapport,contraception,mst, amelioration, ist,
               preservatif, partenaires, prevention, sexualite_precoce, facteurs, risques,
                 age_premier_rapport, acces_sante, protection, education, difficultes, frequence_sante):
        
        
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
        
        return f"""
         <h1>Merci pour votre participation 😁️!</h1>
         <a href="/stats">Voir les statistiques des participants📊️</a><br><br>
         <a href="/">Retour à l'accueil🎲️</a>
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
                       SELECT sexe,COUNT(*) 
                       FROM reponses
                       GROUP BY sexe
                          """)
        repartition_sexe = cursor.fetchall()
        
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
        html += """
            </ul>
             <a href="/">Retour à l'accueil</a>
        </div>
        </body>
        </html>
            """
        
            
        return html
     
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    conf = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(current_dir, 'static')
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': int(os.environ.get('PORT', 8081))
                            })
    cherrypy.quickstart(MonSiteWeb(), '/', conf)
    
