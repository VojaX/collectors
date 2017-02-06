import { Injectable } from '@angular/core'
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/map';

import { Collection } from './collection';

@Injectable()
export class CollectionService {
	private _productUrl ='http://4e98d0e2.ngrok.io/api/collection/';

	constructor(private _http: Http){

	}

	getCollections(): Observable<Collection[]> {
		return this._http.get(this._productUrl)
			.map((response: Response) => <Collection[]> response.json());
	};
	/*$http.get('/api/announcements/'+announcementId+'/').then(function (response) {
                $scope.announcement = response.data;
                // photos
                angular.forEach($scope.announcement.photo_set, function (photo) {
                    $scope.photos.create.push(photo.id);
                    $scope.files.push({id: photo.id, data: photo});
                    if (photo.is_primary) {
                        $scope.photos.primary = photo.id;
                    }
                });
                */
	/*private handleError(error: Response){
		console.error(error);
		return Observable.throw(error.json().error || 'Server error');	
	};*/
}