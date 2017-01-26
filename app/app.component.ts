import { Component } from '@angular/core';

@Component({
	selector: 'cs-app',
	template: `
		<h1>{{pageTitle}}</h1>
		<cs-collection-list></cs-collection-list>
	`
})
export class AppComponent {
	pageTitle: string = 'Collectors stuff';
}