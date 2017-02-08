import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';

import { AppComponent }  from './app.component';
import { CollectionListComponent } from './collection-list/collection-list.component';

@NgModule({
	imports: [ 
		BrowserModule,
		HttpModule
	 ],
	declarations: [
		AppComponent,
		CollectionListComponent
	],
	bootstrap: [ AppComponent ]
})
export class AppModule { }
