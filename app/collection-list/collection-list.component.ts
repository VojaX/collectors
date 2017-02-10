import { Component } from '@angular/core';
import { CollectionService } from './collection.service';
import { Collection } from './collection';

@Component({
	selector: 'cs-collection-list',
	templateUrl: 'app/collection-list/collection-list.component.html'
})

export class CollectionListComponent {
	
	constructor(private _collectionService: CollectionService){
	}
	collections: Collection[];
	errorMessage: string;
	countryFilter: string = '';

	ngOnInit(): void {
		this._collectionService.getCollections()
			.subscribe(collections => this.collections = collections,
				error => this.errorMessage = <any>error);
	}
}