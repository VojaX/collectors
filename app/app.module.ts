import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent }  from './app.component';
import { CollectionFilterPipe } from './collection-list/collection-filter.pipe';
import { CollectionListComponent } from './collection-list/collection-list.component';

@NgModule({
	imports: [ 
		BrowserModule,
		FormsModule,
		HttpModule
	 ],
	declarations: [
		AppComponent,
		CollectionFilterPipe,
		CollectionListComponent
	],
	bootstrap: [ AppComponent ]
})
export class AppModule { }
