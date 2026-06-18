# Définition de la classe Etudiant
class Etudiant:

    # Constructeur : initialise les attributs de l'étudiant
    def __init__(self, matricule, nom, age, filiere):
        self.matricule = matricule      # Numéro matricule de l'étudiant
        self.nom = nom                  # Nom de l'étudiant
        self.age = age                  # Âge de l'étudiant
        self.filiere = filiere          # Filière d'étude
        self.notes = []                 # Liste qui contiendra les notes

    # Méthode pour ajouter une note
    def ajouter_note(self, note):
        # Vérifie que la note est comprise entre 0 et 100
        if 0 <= note <= 100:
            self.notes.append(note)     # Ajoute la note à la liste
            return True                 # ✅ CORRECTION : retourne True si succès
        else:
            print("Note invalide.")
            return False                # ✅ CORRECTION : retourne False si échec

    # Méthode pour modifier une note existante
    def modifier_note(self, index, nouvelle_note):

        # Vérifie si l'index existe dans la liste des notes
        if 0 <= index < len(self.notes):

            # Vérifie que la nouvelle note est valide
            if 0 <= nouvelle_note <= 100:

                ancienne_note = self.notes[index]     # Sauvegarde l'ancienne note
                self.notes[index] = nouvelle_note     # Remplace par la nouvelle note

                print(
                    f"Note modifiée avec succès : "
                    f"{ancienne_note} → {nouvelle_note} pour {self.nom}"
                )
                return True
            else:
                print("Note invalide. La note doit être entre 0 et 100.")
                return False
        else:
            print("Index invalide.")
            return False

    # Méthode pour supprimer une note
    def supprimer_note(self, index):

        # Vérifie si l'index est valide
        if 0 <= index < len(self.notes):

            # Supprime la note et la retourne
            note_supprimee = self.notes.pop(index)

            print(
                f"Note {note_supprimee} supprimée avec succès "
                f"pour {self.nom}."
            )
            return True
        else:
            print(
                f"Erreur : index {index} invalide. "
                f"L'étudiant a {len(self.notes)} note(s)."
            )
            return False

    # Méthode pour calculer la moyenne des notes
    def calculer_moyenne(self):

        # Si aucune note n'est enregistrée
        if len(self.notes) == 0:
            return 0

        # Retourne la moyenne
        return sum(self.notes) / len(self.notes)

    # Méthode qui vérifie si l'étudiant est admis
    def admis(self):

        # L'étudiant est admis si sa moyenne est supérieure ou égale à 60
        return self.calculer_moyenne() >= 60

    # Méthode pour afficher toutes les informations de l'étudiant
    def afficher_infos(self):

        print("\n" + "=" * 50)
        print("INFORMATIONS SUR L'ÉTUDIANT")
        print("=" * 50)

        # Affichage des informations personnelles
        print(f"Matricule : {self.matricule}")
        print(f"Nom : {self.nom}")
        print(f"Âge : {self.age} ans")
        print(f"Filière : {self.filiere}")

        # Vérifie si des notes existent
        if self.notes:

            print("Notes :")

            # Parcourt la liste des notes avec leur index
            for i, note in enumerate(self.notes):
                print(f"[{i}] = {note}")

        else:
            print("Aucune note enregistrée.")

        # Calcul de la moyenne
        moyenne = self.calculer_moyenne()

        # Affichage de la moyenne
        print(f"Moyenne : {moyenne:.2f}/100")

        # Affichage du statut de l'étudiant
        if self.admis():
            print("Statut : Admis (moyenne ≥ 60)")
        else:
            print("Statut : Échec (moyenne < 60)")

        print("=" * 50)

    # Méthode spéciale appelée lors de l'utilisation de print(objet)
    def __str__(self):

        # Retourne une représentation textuelle de l'objet
        return (
            f"{self.matricule} -- {self.nom} "
            f"({self.filiere}) "
            f"Moyenne : {self.calculer_moyenne():.2f}"
        )
