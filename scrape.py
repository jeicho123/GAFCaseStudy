import requests
import json

url = "https://platform.cloud.coveo.com/rest/search/v2?organizationId=gafmaterialscorporationproduction3yalqk12"

headers = {
    "Authorization": "Bearer xx3cfe6ca4-11f2-45b6-83ad-41e053e06504",
    "Content-Type": "application/json"
}

payload = {
  "locale": "en-US",
  "debug": False,
  "tab": "default",
  "referrer": "https://www.gaf.com/en-us/roofing-contractors/commercial?postalCode=10013&countryCode=us&distance=50",
  "timezone": "America/New_York",
  "visitorId": "c26a2b83-7259-4309-b8f6-e17a77b7b48c",
  "actionsHistory": [
    {"name": "Query", "time": "\"2025-05-22T14:36:46.246Z\""},
    {"name": "Query", "time": "\"2025-05-22T14:35:02.596Z\""},
    {"name": "Query", "time": "\"2025-05-22T14:33:27.109Z\""},
    {"name": "Query", "time": "\"2025-05-22T03:18:19.218Z\""},
    {"name": "Query", "time": "\"2025-05-21T18:01:26.850Z\""},
    {"name": "Query", "time": "\"2025-05-21T02:24:10.926Z\""}
  ],
  "aq": "@distanceinmiles <= 25 AND @gaf_f_country_code = USA",
  "context": {
    "sortingStrategy": "gafrecommended-initial"
  },
  "fieldsToInclude": [
    "author", "language", "urihash", "objecttype", "collection", "source", "permanentid",
    "gaf_featured_image_src", "gaf_featured_image_alt", "gaf_contractor_id", "gaf_contractor_type",
    "gaf_contractor_dba", "gaf_navigation_title", "gaf_rating", "gaf_number_of_reviews",
    "gaf_f_city", "gaf_f_state_code", "gaf_f_contractor_certifications_and_awards", "gaf_phone",
    "uri", "gaf_f_contractor_technologies", "gaf_latitude", "gaf_longitude", "distance",
    "distanceinmiles", "gaf_postal_code", "gaf_f_country_code", "gaf_enrolled_in_gaf_leads",
    "UniqueId", "Uri"
  ],
  "pipeline": "prod-gaf-recommended-residential-contractors",
  "q": "",
  "enableQuerySyntax": False,
  "searchHub": "prod-gaf-recommended-residential-contractors",
  "sortCriteria": "relevancy",
  "analytics": {
    "clientId": "c26a2b83-7259-4309-b8f6-e17a77b7b48c",
    "clientTimestamp": "2025-05-22T14:36:46.340Z",
    "documentReferrer": "https://www.gaf.com/en-us/roofing-contractors/commercial?postalCode=10013&countryCode=us&distance=50",
    "originContext": "Search",
    "actionCause": "interfaceChange",
    "customData": {
      "context_sortingStrategy": "gafrecommended-initial",
      "coveoHeadlessVersion": "2.19.0",
      "interfaceChangeTo": "default"
    }
  },
  "facets": [
    {
      "filterFacetCount": True,
      "injectionDepth": 1000,
      "numberOfValues": 999,
      "sortCriteria": "automatic",
      "type": "specific",
      "currentValues": [],
      "freezeCurrentValues": False,
      "isFieldExpanded": False,
      "preventAutoSelect": False,
      "field": "gaf_f_contractor_specialties",
      "resultsMustMatch": "allValues",
      "facetId": "gaf_f_contractor_specialties"
    },
    {
      "filterFacetCount": True,
      "injectionDepth": 1000,
      "numberOfValues": 999,
      "sortCriteria": "automatic",
      "type": "specific",
      "currentValues": [],
      "freezeCurrentValues": False,
      "isFieldExpanded": False,
      "preventAutoSelect": False,
      "field": "gaf_f_contractor_technologies",
      "resultsMustMatch": "atLeastOneValue",
      "facetId": "gaf_f_contractor_technologies"
    },
    {
      "filterFacetCount": True,
      "injectionDepth": 1000,
      "numberOfValues": 999,
      "sortCriteria": "automatic",
      "type": "specific",
      "currentValues": [],
      "freezeCurrentValues": False,
      "isFieldExpanded": False,
      "preventAutoSelect": False,
      "field": "gaf_f_contractor_specialties",
      "facetId": "gaf_f_contractor_specialties_1"
    },
    {
      "filterFacetCount": True,
      "injectionDepth": 1000,
      "numberOfValues": 999,
      "sortCriteria": "automatic",
      "type": "specific",
      "currentValues": [],
      "freezeCurrentValues": False,
      "isFieldExpanded": False,
      "preventAutoSelect": False,
      "field": "gaf_f_contractor_specialties",
      "facetId": "gaf_f_contractor_specialties_2"
    },
    {
      "filterFacetCount": True,
      "injectionDepth": 1000,
      "numberOfValues": 4,
      "sortCriteria": "descending",
      "rangeAlgorithm": "even",
      "currentValues": [
        {"endInclusive": True, "state": "idle", "start": 1, "end": 5},
        {"endInclusive": True, "state": "idle", "start": 2, "end": 5},
        {"endInclusive": True, "state": "idle", "start": 3, "end": 5},
        {"endInclusive": True, "state": "idle", "start": 4, "end": 5}
      ],
      "preventAutoSelect": False,
      "type": "numericalRange",
      "field": "gaf_rating",
      "generateAutomaticRanges": False,
      "facetId": "gaf_rating"
    },
    {
      "filterFacetCount": True,
      "injectionDepth": 1000,
      "numberOfValues": 0,
      "sortCriteria": "ascending",
      "rangeAlgorithm": "even",
      "currentValues": [],
      "preventAutoSelect": False,
      "type": "dateRange",
      "field": "date",
      "generateAutomaticRanges": False,
      "facetId": "date"
    }
  ],
  "numberOfResults": 10,
  "firstResult": 0,
  "facetOptions": {
    "freezeFacetOrder": False
  },
  "queryFunctions": [
    {
      "fieldName": "@distanceinmiles",
      "function": "dist(@gaf_latitude, @gaf_longitude, 40.7217861, -74.0094471)*0.000621371"
    }
  ]
}

response = requests.post(url=url, headers=headers, json=payload).json()["results"]

companies = []
for result in response:
    company_name = result['title']
    company_link = result['uri']
    companies.append({
        'name': company_name,
        'link': company_link
    })

with open('companies.json', 'w', encoding='utf-8') as f:
    json.dump(companies, f, indent=2, ensure_ascii=False)