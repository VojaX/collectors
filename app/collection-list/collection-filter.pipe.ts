import { PipeTransform, Pipe } from '@angular/core';
import { Collection } from './collection';

@Pipe({
	name: 'countryPipe'
})
export class CollectionFilterPipe implements PipeTransform {
	transform(collections: Collection[], keyWord: string): Collection[] { 
		keyWord = keyWord ? keyWord.toLocaleLowerCase() : null;
		return keyWord ? collections.filter((collection: Collection) => 
			collection.country.name.toLocaleLowerCase().indexOf(keyWord) !== -1) : collections;
	};
}