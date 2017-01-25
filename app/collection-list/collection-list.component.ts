import { Component } from '@angular/core';

@Component({
	selector: 'cs-collection-list',
	templateUrl: 'app/collection-list/collection-list.component.html'
})
export class CollectionListComponent {
	collections: any[] = [
		{
			"category": "money",
			"type": "banknotes",
			"subtype": "polish",
			"name": "Polskie banknoty z lat 1925 - 1929",
			"set": "Ser. X. , Ser. X.X. oraz Ser. XX",
			"count": 3,
			"numeration": "",
			"releaseDate": "20 august 1926 and 20 august 1929",
			"country": "Poland",
			"description": "Water mark: image of Bolesław Chrobry and dates: 992 and 1125 or 10 ZŁ. Size: 160 mm x 80 mm",
			"faceImage": "https://upload.wikimedia.org/wikipedia/commons/7/7e/10_z%C5%82otych_1929_r._AWERS.jpg",
			"reverseImage": "https://upload.wikimedia.org/wikipedia/commons/a/a4/10_z%C5%82otych_1929_r._REWERS.jpg",
			"likes": 1222,
			"usersPossesing": 3,
			"tags": "polish bill 10 20 50 zloty złoty chrobry boleslaw bolesław"
		},
		{
			"category": "pogs/caps",
			"type": "tazos",
			"subtype": "pokemon",
			"name": "Pokemon Tazo 1",
			"set": "Set 1",
			"count": 51,
			"numeration": "1 - 51",
			"releaseDate": "2000 - 2001",
			"country": "Poland",
			"description": "Made of plastic in a shape of a circle. Has a diameter of 40mm and thickness of 1mm. They are painted by paint/ink. Easy to clash and smooth. On the pogs you can see pokemons from range of 1 - 151 (pokedex numeration) These pokemons are only the one which can evolve (in their base form) and Ash (Tazo 51). These tazos have got a bug in translation on their front. Instead of using polish 'Typ' which means 'Type' they used polish 'Siła' which means 'Force'.",
			"faceImage": "http://i.imgur.com/lv7rh29.jpg",
			"reverseImage": "http://i.imgur.com/x7ppUnl.jpg",
			"likes": 11111,
			"usersPossesing": 6,
			"tags": "pokemon tazo set 1 polish polska poland"
		}
	];
}