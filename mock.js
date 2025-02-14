const classes = ['6emeA', '6emeB', '6emeC', '6emeD', '6emeE', '5emeA', '5emeB', '5emeC', '5emeD', '5emeE',
                '4emeA', '4emeB', '4emeC', '4emeD', '4emeE', '3emeA', '3emeB', '3emeC', '3emeD', '3emeE'];

// Liste de noms et prénoms français courants
const noms = ['Martin', 'Bernard', 'Thomas', 'Petit', 'Robert', 'Richard', 'Durand', 'Dubois', 'Moreau', 'Laurent',
             'Simon', 'Michel', 'Lefebvre', 'Leroy', 'Roux', 'David', 'Bertrand', 'Morel', 'Fournier', 'Girard'];

const prenoms = ['Jean', 'Pierre', 'Michel', 'André', 'Philippe', 'René', 'Louis', 'Alain', 'Jacques', 'Bernard',
                'Marie', 'Jeanne', 'Catherine', 'Françoise', 'Anne', 'Monique', 'Isabelle', 'Sophie', 'Martine', 'Nicole'];

// Fonction pour générer une date aléatoire dans une plage
function randomDate(start, end) {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}

// Fonction pour formater la date au format demandé
function formatDate(date) {
    return date.toISOString().replace('T', ' ').slice(0, 19);
}

// Fonction pour générer des voeux uniques
function generateUniqueChoices() {
    let choices = Array.from({length: 7}, (_, i) => `Programme ${i + 1}`);
    let result = [];
    for(let i = 0; i < 3; i++) {
        const index = Math.floor(Math.random() * choices.length);
        result.push(choices[index]);
        choices.splice(index, 1);
    }
    return result;
}

// Générer 540 entrées
let data = [];
for(let i = 0; i < 540; i++) {
    const dateSubmission = randomDate(new Date(2025, 1, 1), new Date(2025, 1, 14));
    const nom = noms[Math.floor(Math.random() * noms.length)];
    const prenom = prenoms[Math.floor(Math.random() * prenoms.length)];
    const classe = classes[Math.floor(Math.random() * classes.length)];
    const voeux = generateUniqueChoices();
    
    data.push([
        formatDate(dateSubmission),
        nom,
        prenom,
        classe,
        voeux[0],
        voeux[1],
        voeux[2]
    ].join(';'));
}

// Trier par date
data.sort();

// Afficher quelques exemples
console.log('Exemple des 5 premières lignes :');
console.log(data.slice(0, 5).join('\n'));
console.log('\nExemple des 5 dernières lignes :');
console.log(data.slice(-5).join('\n'));

// Préparer le fichier CSV
const csv = data.join('\n');
console.log('\nNombre total d\'entrées :', data.length);