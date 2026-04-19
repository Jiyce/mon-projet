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
           <title>ACCUEIL</title>
           <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body>
            <div class="container">
                <h1><i>SANTE SEXUELLE ET REPRODUCTIVE</i></h1>
                <p> 
                 Cette application a pour but d'évaluer les connaissances en matière de  santé sexuelle et reproductive chez les jeunes. Les données collectées sont anonymes et serviront à des fins éducatives.
                </p>
        
                <a href="questionnaire">
                    <button>Commencer le questionnaire</button>
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
        <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        
        <body>
        <div class="container">
        
        <h1><i>Questionnaire de santé sexuelle et reproductive</i></h1>
        <p>Veuillez répondre aux questions suivantes :</p>
        
        <form method="post" action="submit">
        
        <label>Age : </label>
            <select name="age" required>
                <option value="15-19">15-19 ans</option>
                <option value="20-25">20-25 ans</option>
                <option value="25-30">25-30 ans</option>
                <option value="30+">30 ans et plus</option>
            </select><br><br>
            
        <label>Sexe : </label>
            <select name="sexe" required>
                <option value=" Homme">Homme</option>
                <option value="Femme">Femme</option>
            </select><br><br>
            
        <label>Avez-vous déjà participez à une campagne de sensibilisation sur la santé sexuelle et reproductive ?</label>
        <input type="radio" id="oui" name="sensibilisation" value="Oui" >Oui
        <input type="radio" id="non" name="sensibilisation" value="Non" >Non<br><br>
        
        <label>Etes_vous sexuellement actif ?</label>
        <input type="radio" id="oui" name="dernier_rapport" value="Oui" required>
        <label for="oui">Oui</label>
        <input type="radio" id="non" name="dernier_rapport" value="Non" required>
        <label for="non">Non</label><br><br>
        
        <label>Age du premier rapport sexuel :</label>
            <input type="number" name="age_premier_rapport" min="10" max="50" required><br><br>
            
        <label>Combien de partenaires sexuels avez-vous eu au cours de votre vie ? :</label>
            <select name="partenaires" required>
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2-5">2-5</option>
                <option value="5+">5 et plus</option>
            </select><br><br>
            
        <label>Quelle méthode de contraception utilisez-vous ?</label>
            <select name="contraception" required>
                <option value="Aucune">Aucune</option>
                <option value="Préservatif">Préservatif</option>
                <option value="Pilule">Pilule</option>
                <option value="Stérilet">Stérilet</option>
                <option value="Autre">Autre</option>
            </select><br><br>
            
        <label>Avez-vous déjà été testé pour les infections sexuellement transmissibles (ist) ?</label>
        <input type="radio" id="oui" name="ist" value="Oui" required>
        <label for="oui">Oui</label>
        <input type="radio" id="non" name="ist" value="Non" required>
        <label for="non">Non</label><br><br> 
            
        <label>Le préservatif est-il efficace pour prévenir les grossesses et les ist ?</label>
        <input type="radio" id="oui" name="preservatif" value="Oui" required>
        <label for="oui">Oui</label><br>
        <input type="radio" id="non" name="preservatif" value="Non" required>
        <label for="non">Non</label><br><br>
            
        <label>Quelles sont les différentes maladies sexuellement transmissibles (mst) que vous connaissez ?</label>
            <input type="text" name="mst" required><br><br>
        
        <label>Avez-vous déjà consulter un professionnel de santé?</label>
           <input type="radio" id="oui" name="acces_sante" value="Oui" required>
            <label for="oui">Oui</label>
            <input type="radio" id="non" name="acces_sante" value="Non" required>
            <label for="non">Non</label><br><br>
        
        <label>Utilisez-vous toujours une protection lors de vos rapports sexuels ?</label>
            <input type="radio" id="oui" name="protection" value="Oui" required>
            <label for="oui">Oui</label>
            <input type="radio" id="non" name="protection" value="Non" required>
            <label for="non">Non</label><br><br>
        
        <label>Pensez-vous que l'éducation sexuelle est suffisante ?</label>
            <input type="radio" id="oui" name="education" value="Oui" required>
            <label for="oui">Oui</label>
            <input type="radio" id="non" name="education" value="Non" required>
            <label for="non">Non</label><br><br>

         <label>Comment amélioreriez-vous l'accès à l'éducation sexuelle et aux services de santé reproductive pour les jeunes ?</label>
        <input type="text" name="amelioration" required><br><br>
            
        <input type="submit" value="Soumettre">         
        </form>
        
        </div>
        </body>
        </html>
        '''
    # Traitement des données du formulaire
    
    @cherrypy.expose
    def submit(self,age, sexe, sensibilisation,dernier_rapport,contraception,mst, amelioration, ist, preservatif, partenaires,
                   age_premier_rapport, acces_sante, protection, education):
        
        
        conn = self.connexion_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reponses (age, sexe, sensibilisation,dernier_rapport,contraception,mst, amelioration, ist, preservatif, partenaires, age_premier_rapport, acces_sante, protection, education) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (age, sexe, sensibilisation,dernier_rapport,contraception,mst, amelioration, ist, preservatif, 
                        partenaires, age_premier_rapport, acces_sante, protection, education))
        conn.commit()
        conn.close()
        
        return f"""
         <h1>Merci pour votre participation !</h1>
         <a href="/">Retour à l'accueil</a>
         """
    
    @cherrypy.expose
    def stats(self):
        conn = self.connexion_db()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM  reponses")
        total, moyenne = cursor.fetchone()[0]
        
        cursor.execute("""
                       SELECT sexe,COUNT(*) 
                       FROM reponses
                       GROUP BY sexe
                          """)
        repartition_sexe = cursor.fetchall()
        conn.close()
        
        html = f"""
        <h1>Statistiques des participants</h1>
        <p><strong>Nombre total de participants : </strong> {total}</p>
        <p><strong>Score moyen :</strong> {moyenne:.2f}/3</p>
        
            <a href="/">Retour à l'accueil</a>
        """
        return html
     
if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': int(os.environ.get('PORT', 8081))
                            })
    conf = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir':  'static'
        }
    }
    cherrypy.quickstart(MonSiteWeb(), config="tutoriel.conf")
    