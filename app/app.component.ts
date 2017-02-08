import { Component } from '@angular/core';
import { CollectionService } from './collection-list/collection.service';

@Component({
	selector: 'cs-app',
	template: `
		<h1>{{pageTitle}}</h1>
		<cs-collection-list></cs-collection-list>
	`,
	providers: [CollectionService]
})

export class AppComponent {
	pageTitle: string = 'Collectors stuff';
}