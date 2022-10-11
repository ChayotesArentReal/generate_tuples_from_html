# generate_tuples_from_html
Generate tuples from html text

Example
python3 main.py -url https://starwars.fandom.com/wiki/Kyber_crystal

[('unimaginable', 'axe'), ('search', 'unable'), ('accidentally', 'built'), ('iii', 'wish'), ('shunt', 'general'), ('noted', 'episode'), ('kind', 'two'), ('rebel', 'larger'), ('freighter', 'death'), ('permutations', 'updated'), ('fault', 'alliance'), ('energizer', 'plasma'), ('major', 'voice'), ('superweapons', 'year'), ('voice', 'cad'), ('circuit', 'empire'), ('expose', 'general'), ('violent', 'fault'), ('cho', 'nearby'), ('long', 'thirteen'), ('intricate', 'training'), ('third', 'treasure'), ('padawan', 'battlefront'), ('became', 'green'), ('variety', 'atlas'), ('ice', 'striking'), ('main', 'multiple'), ('guard', 'inside'), ('category', 'prime'), ('mined', 'knight'), ('lasing', 'construct'), ('pure', 'comparable'), ('ranks', 'vow'), ('rendezvous', 'shiim'), ('protosaber', 'lattice'), ('shop', 'shoto'), ('den', 'hassk'), ('least', 'ancient'), ('forgotten', 'looks'), ('fandoms', 'harness'), ('strike', 'introduction'), ('containers', 'near'), ('memory', 'years'), ('heir', 'inert'), ('return', 'society'), ('calendar', 'nearby'), ('enormous', 'shifts'), ('entire', 'collimating'), ('angle', 'caused'), ('vii', 'discover')]



# Install
1. Install python dependencies
```bash
pip install -r requirements.txt
```

2. Import nltk stopwords
```python
import nltk
nltk.download('stopwords')
```

# Usage
```bash
python3 main.py -url https://starwars.fandom.com/wiki/Kyber_crystal
```

