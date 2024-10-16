/* tslint:disable */
/* eslint-disable */
/**
 * chomestatus API
 * The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface SetStarRequest
 */
export interface SetStarRequest {
    /**
     * 
     * @type {number}
     * @memberof SetStarRequest
     */
    featureId?: number;
    /**
     * 
     * @type {boolean}
     * @memberof SetStarRequest
     */
    starred?: boolean;
}

/**
 * Check if a given object implements the SetStarRequest interface.
 */
export function instanceOfSetStarRequest(value: object): value is SetStarRequest {
    return true;
}

export function SetStarRequestFromJSON(json: any): SetStarRequest {
    return SetStarRequestFromJSONTyped(json, false);
}

export function SetStarRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): SetStarRequest {
    if (json == null) {
        return json;
    }
    return {
        
        'featureId': json['featureId'] == null ? undefined : json['featureId'],
        'starred': json['starred'] == null ? undefined : json['starred'],
    };
}

export function SetStarRequestToJSON(value?: SetStarRequest | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'featureId': value['featureId'],
        'starred': value['starred'],
    };
}
