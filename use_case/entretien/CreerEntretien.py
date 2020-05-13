class CreerEntretien:
    def create(self, demande):
        recruteur = recruteurRepository.trouveRecruteurDisponible(demande.getHoraireEntretien())
        salle = salleRepository.trouverSalleLibre(demande.getHoraireEntretien())
        nouvelEntretien= entretienRepository.create(demande.getCandidat(), demande.getHoraireEntretien(), recruteur)
