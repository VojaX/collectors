import { Injectable } from '@angular/core'
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/map';

import { Collection } from './collection';

@Injectable()
export class CollectionService {
	private _productUrl ='https://06ba8ce0.ngrok.io/api/collection/';

	constructor(private _http: Http){

	}

	getCollections(): Observable<Collection[]> {
		return this._http.get(this._productUrl)
			.map((response: Response) => <Collection[]> response.json());
	};
	/*private handleError(error: Response){
		console.error(error);
		return Observable.throw(error.json().error || 'Server error');	
	};*/
}