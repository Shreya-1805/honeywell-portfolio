import { LightningElement, api, wire } from 'lwc';
import getAssets from '@salesforce/apex/AssetHealthController.getAssets';

export default class AssetHealth extends LightningElement {
    @api recordId; // Account Id when placed on an Account page
    assets = [];
    error;

    @wire(getAssets, { accountId: '$recordId' })
    wired({ data, error }) {
        if (data) {
            this.assets = data.map(a => ({
                ...a,
                openCases: a.Cases ? a.Cases.length : 0,
                badge: a.Cases && a.Cases.length ? 'slds-theme_error' : 'slds-theme_success'
            }));
            this.error = undefined;
        } else if (error) {
            this.error = error.body ? error.body.message : 'Unknown error';
        }
    }
}
