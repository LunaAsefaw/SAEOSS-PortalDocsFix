# -*- coding: utf-8 -*-

"""The constants variables"""

import enum
import typing

ISO_TOPIC_CATEGORIES: typing.Final[typing.List[typing.Tuple[str, str]]] = [
    ("farming", "Farming"),
    ("biota", "Biota"),
    ("boundaries", "Boundaries"),
    ("climatologyMeteorologyAtmosphere", "Climatology, Meteorology, Atmosphere"),
    ("economy", "Economy"),
    ("elevation", "Elevation"),
    ("environment", "Environment"),
    ("geoscientificInformation", "Geoscientific Information"),
    ("health", "Health"),
    ("imageryBaseMapsEarthCover", "Imagery, Basemaps, Earth Cover"),
    ("intelligenceMilitary", "Intelligence, Millitary"),
    ("inlandWaters", "Inland Waters"),
    ("location", "Location"),
    ("oceans", "Oceans"),
    ("planningCadastre", "Planning, Cadastre"),
    ("society", "Society"),
    ("structure", "Structure"),
    ("transportation", "Transportation"),
    ("utilitiesCommuinication", "Utilities, Communication"),
]

SANSA_ORG_NAME = "sansa"


class DatasetManagementActivityType(enum.Enum):
    REQUEST_MAINTENANCE = "requested dataset maintenance"
    REQUEST_PUBLICATION = "requested dataset publication"

DATASET_MINIMAL_SET_OF_FIELDS = [
    "title",
    "name",
    "notes",
    "responsible_party-0-individual_name",
    "responsible_party-0-role",
    "responsible_party-0-position_name",
    "metadata_reference_date_and_stamp-0-reference",
    "metadata_reference_date_and_stamp-0-reference_date_type",
    "topic_and_sasdi_theme-0-iso_topic_category",
    "owner_org",
    "private",
    "metadata_language_and_character_set-0-dataset_language",
    "metadata_language_and_character_set-0-metadata_language",
    "metadata_language_and_character_set-0-dataset_character_set",
    "metadata_language_and_character_set-0-metadata_character_set",
    "lineage_statement",
    "distribution_format-0-name",
    "distribution_format-0-version",
    "spatial",
    "spatial_parameters-0-equivalent_scale",
    "spatial_parameters-0-spatial_representation_type",
    "spatial_parameters-0-spatial_reference_system",
    "metadata_reference_date_and_stamp-0-stamp",
    "metadata_reference_date_and_stamp-0-stamp_date_type",
]

DATASET_FULL_SET_OF_FIELDS = [
    "title",
    "name",
    "featured",
    "doi",
    "metadata_standard-0-name",
    "metadata_standard-0-version",
    "notes",
    "responsible_party-0-individual_name",
    "responsible_party-0-position_name",
    "responsible_party-0-role",
    "responsible_party-0-electronic_mail_address",
    "responsible_party_contact_address-0-delivery_point",
    "responsible_party_contact_address-0-city",
    "responsible_party_contact_address-0-administrative_area",
    "responsible_party_contact_address-0-postal_code",
    "responsible_party_contact_info-0-voice",
    "responsible_party_contact_info-0-facsimile",
    "contact-0-individual_name",
    "contact-0-position_name",
    "contact-0-role",
    "contact-0-electronic_mail_address",
    "contact_address-0-delivery_point",
    "contact_address-0-city",
    "contact_address-0-administrative_area",
    "contact_address-0-postal_code",
    "contact_information-0-voice",
    "contact_information-0-facsimile",
    "owner_org",
    "private",
    "metadata_reference_date_and_stamp-0-reference",
    "metadata_reference_date_and_stamp-0-reference_date_type",
    "topic_and_sasdi_theme-0-iso_topic_category",
    "topic_and_sasdi_theme-0-sasdi_theme",
    "tag_string",
    "metadata_record_format-0-name",
    "metadata_record_format-0-version",
    "metadata_language_and_character_set-0-dataset_language",
    "metadata_language_and_character_set-0-metadata_language",
    "metadata_language_and_character_set-0-dataset_character_set",
    "metadata_language_and_character_set-0-metadata_character_set",
    "lineage_statement",
    "distribution_format-0-name",
    "distribution_format-0-version",
    "online_resource-0-name",
    "online_resource-0-linkeage",
    "online_resource-0-description",
    "online_resource-0-application_profile",
    "spatial",
    "spatial_parameters-0-equivalent_scale",
    "spatial_parameters-0-spatial_representation_type",
    "spatial_parameters-0-spatial_reference_system",
    "reference_system_additional_info",
    "metadata_reference_date_and_stamp-0-stamp",
    "metadata_reference_date_and_stamp-0-stamp_date_type",
]

XML_DATASET_NAMING_MAPPING = {
    "title": "title",
    "name": "name",
    "featured": "featured",
    "doi": "doi",
    "notes": "notes",
    "private": "private",
    "tagString": "tag_string",
    "MetadataStandardName": "metadata_standard-0-name",
    "MetadataStandardVersion": "metadata_standard-0-version",
    "OwnerOrg": "owner_org",
    "ResponsiblePartyIndividualName": "responsible_party-0-individual_name",
    "ResponsiblePartyRole": "responsible_party-0-role",
    "ResponsiblePartyPositionName": "responsible_party-0-position_name",
    "ResponsiblePartyElectronicMailAddress": "responsible_party-0-electronic_mail_address",
    "ResponsiblePartyContactAddressDeliveryPoint": "responsible_party_contact_address-0-delivery_point",
    "ResponsiblePartyContactAddressCity": "responsible_party_contact_address-0-city",
    "ResponsiblePartyContactAddressAdministrativeArea": "responsible_party_contact_address-0-administrative_area",
    "ResponsiblePartyContactAddressPostalCode": "responsible_party_contact_address-0-postal_code",
    "ResponsiblePartyContactInfoVoice": "responsible_party_contact_info-0-voice",
    "ResponsiblePartyContactInfoFacsimile": "responsible_party_contact_info-0-facsimile",
    "ReferenceDate": "metadata_reference_date_and_stamp-0-reference",
    "ReferenceDateType": "metadata_reference_date_and_stamp-0-reference_date_type",
    "IsoTopicCategory": "topic_and_sasdi_theme-0-iso_topic_category",
    "LineageStatement": "lineage_statement",
    "DatasetLanguage": "metadata_language_and_character_set-0-dataset_language",
    "MetadataLanguage": "metadata_language_and_character_set-0-metadata_language",
    "DatasetCharacterset": "metadata_language_and_character_set-0-dataset_character_set",
    "MetadataCharacterset": "metadata_language_and_character_set-0-metadata_character_set",
    "DistributionFormatName": "distribution_format-0-name",
    "DistributionFormatVersion": "distribution_format-0-version",
    "spatial": "spatial",
    "EquivalentScale": "spatial_parameters-0-equivalent_scale",
    "SpatialRepresentationType": "spatial_parameters-0-spatial_representation_type",
    "SpatialReferenceSystem": "spatial_parameters-0-spatial_reference_system",
    "StampDate": "metadata_reference_date_and_stamp-0-stamp",
    "StampDateType": "metadata_reference_date_and_stamp-0-stamp_date_type",
    "ContactIndividualName": "contact-0-individual_name",
    "ContactPositionName": "contact-0-position_name",
    "ContactRole": "contact-0-role",
    "ContactElectronicMailAddress": "contact-0-electronic_mail_address",
    "ContactAddressDeliveryPoint": "contact_address-0-delivery_point",
    "ContactAddressCity": "contact_address-0-city",
    "ContactAddressAdministrativeArea": "contact_address-0-administrative_area",
    "ContactAddressPostalCode": "contact_address-0-postal_code",
    "ContactInformationVoice": "contact_information-0-voice",
    "ContactInformationFacsimile": "contact_information-0-facsimile",
}

# this is necessary to ensure consistancy with saeon extra names

DATASET_SUBFIELDS_MAPPING = {
    "metadata_standard-0-name": "metadata_standard",
    "metadata_standard-0-version": "metadata_standard_version",
    "responsible_party-0-individual_name": "responsible_party_individual_name",
    "responsible_party-0-role": "responsible_party_role",
    "responsible_party-0-position_name": "responsible_party_position_name",
    "responsible_party-0-electronic_mail_address": "responsible_party_electronic_mail_address",
    "responsible_party_contact_address-0-delivery_point": "responsible_party_contact_address_delivery_point",
    "responsible_party_contact_address-0-city": "responsible_party_contact_address_city",
    "responsible_party_contact_address-0-administrative_area": "responsible_party_contact_address_administrative_area",
    "responsible_party_contact_address-0-postal_code": "responsible_party_contact_address_postal_code",
    "responsible_party_contact_info-0-voice": "responsible_party_contact_info_voice",
    "responsible_party_contact_info-0-facsimile": "responsible_party_contact_info_facsimile",
    "metadata_reference_date_and_stamp-0-reference": "reference_date",
    "metadata_reference_date_and_stamp-0-reference_date_type": "reference_datetype",
    "metadata_reference_date_and_stamp-0-stamp": "stamp_date",
    "metadata_reference_date_and_stamp-0-stamp_date_type": "stamp_datetype",
    "topic_and_sasdi_theme-0-iso_topic_category": "iso_topic_category",
    "lineage_statement": "lineage_statement",
    "metadata_language_and_character_set-0-dataset_language": "dataset_language",
    "metadata_language_and_character_set-0-metadata_language": "metadata_language",
    "metadata_language_and_character_set-0-dataset_character_set": "dataset_character_set",
    "metadata_language_and_character_set-0-metadata_character_set": "metadata_character_set",
    "distribution_format-0-name": "format_name",
    "distribution_format-0-version": "format_version",
    "spatial_parameters-0-equivalent_scale": "equivalent_scale",
    "spatial_parameters-0-spatial_representation_type": "spatial_representation_type",
    "spatial_parameters-0-spatial_reference_system": "spatial_reference_system",
    "contact-0-individual_name": "contact_individual_name",
    "contact-0-position_name": "contact_position_name",
    "contact-0-role": "contact_role",
    "contact-0-electronic_mail_address": "contact_electronic_mail_address",
    "contact_address-0-delivery_point": "contact_address_delivery_point",
    "contact_address-0-city": "contact_address_city",
    "contact_address-0-administrative_area": "contact_address_administrative_area",
    "contact_address-0-postal_code": "contact_address_postal_code",
    "contact_information-0-voice": "contact_information_voice",
    "contact_information-0-facsimile": "contact_information_facsimile"
}



DATASET_Harvest_MINIMAL_SET_OF_FIELDS_MAPPING = {
    "guid":"id",
    "id":"id",
    "title":"title",
    "name":"name",
    "metadata_standard_name":"metadata_standard-0-name",
    "metadata_standard_version":"metadata_standard-0-version",
    "notes":"notes",
    "owner_org":"owner_org",
    "responsible_party_individual_name":"responsible_party-0-individual_name",
    "responsible_party_role":"responsible_party-0-role",
    "topic_category":"topic_and_sasdi_theme-0-iso_topic_category",
    "dataset_language":"metadata_language_and_character_set-0-dataset_language",
    "metadata_language":"metadata_language_and_character_set-0-metadata_language",
    "dataset_character_set":"metadata_language_and_character_set-0-dataset_character_set",
    "metadata_character_set":"metadata_language_and_character_set-0-metadata_character_set",
    "lineage":"lineage",
    "contact_organisation": "contact-0-organisation_name",
    "contact_individual_name": "contact-0-individual_name",
    "distribution_format_name":"distribution_format-0-name",
    "distribution_format_version":"distribution_format-0-version",
    "spatial":"spatial",
    "equivalent_scale":"spatial_parameters-0-equivalent_scale",
    "representation_type":"spatial_parameters-0-spatial_representation_type",
    "spatial_reference_system":"spatial_parameters-0-spatial_reference_system", # this needs handling
    "reference_date":"dataset_reference_date-0-reference",
    "dataset_reference_date":"dataset_reference_date-0-reference",
    "dataset_reference_date_type":"dataset_reference_date-0-reference_date_type",
    "metadata_date":"metadata_date",
}



class DCPRRequestRequiredFields(enum.Enum):
    DATASET_LANGUAGE = "en"
    DATASET_CHARACTER_SET = "ucs-2"
    METADATA_CHARACTER_SET = "ucs-2"
    DISTRIBUTION_FORMAT_NAME = "Electronic Metadata Record"
    DISTRIBUTION_FORMAT_VERSION = "1.0"
    EQUIVALENT_SCALE = "10"
    ISO_TOPIC_CATEGORY = "location"
    LINEAGE_LEVEL = "001"
    LINEAGE_STATEMENT = "Formed from a DCPR request"
    LINEAGE_PROCESS_DESCRIPTION = "Formed from a DCPR request"
    METADATA_LANGUAGE = "en"
    METADATA_STANDARD_NAME = "SANS 1878"
    METADATA_STANDARD_VERSION = "1.1"
    NOTES = "Default notes"
    PURPOSE = "Purpose"
    SPATIAL_REFERENCE_SYSTEM = "EPSG:4326"
    SPATIAL_REPRESENTATION_TYPE = "001"
    STATUS = "completed"
    REFERENCE_DATE_TYPE = "Creation"
    STAMP_DATE_TYPE = "Creation"
    RESPONSIBLE_PARTY_INDIVIDUAL_NAME = "individual_name"
    RESPONSIBLE_PARTY_POSITION_NAME = "dataset custodian"
    RESPONSIBLE_PARTY_ROLE = "originator"


PROJECTION = {
    "32737": "UTM37S",
    "32733": "UTM33S",
    "32738": "UTM38S",
    "32734": "UTM34S",
    "32732": "UTM32S",
    "32735": "UTM35S",
    "32629": "UTM29N",
    "32731": "UTM31S",
    "32736": "UTM36S",
    "32739": "UTM39S",
    "32627": "UTM27N",
    "32740": "UTM40S",
    "32638": "UTM38N",
    "32609": "UTM09N",
    "32643": "UTM43N",
    "32630": "UTM30N",
    "32619": "UTM19N",
    "32751": "UTM51S",
    "32728": "UTM28S",
    "32724": "UTM24S",
    "32729": "UTM29S",
    "32621": "UTM21N",
    "32633": "UTM33N",
    "32628": "UTM28N",
    "32634": "UTM34N",
    "32730": "UTM30S",
    "32757": "UTM57S",
    "32727": "UTM27S",
    "32637": "UTM37N",
    "32631": "UTM31N",
    "32615": "UTM15N",
    "32752": "UTM52S",
    "32623": "UTM23N",
    "32635": "UTM35N",
    "32636": "UTM36N",
    "32750": "UTM50S",
    "32749": "UTM49S",
    "32632": "UTM32N",
    "32654": "UTM54N",
    "32613": "UTM13N",
    "32614": "UTM14N",
    "32617": "UTM17N",
    "32719": "UTM19S",
    "32626": "UTM26N",
    "32625": "UTM25N",
    "32624": "UTM24N",
    "32622": "UTM22N",
    "32745": "UTM45S",
    "32649": "UTM49N",
    "32718": "UTM18S",
    "32717": "UTM17S",
    "32754": "UTM54S",
    "32753": "UTM53S",
    "32640": "UTM40N",
    "32639": "UTM39N",
    "32723": "UTM23S",
    "32648": "UTM48N",
    "32760": "UTM60S",
    "32644": "UTM44N",
    "32748": "UTM48S",
    "32612": "UTM12N",
    "32755": "UTM55S",
    "32641": "UTM41N",
    "32652": "UTM52N",
    "32616": "UTM16N",
    "32646": "UTM46N",
    "32642": "UTM42N",
    "32610": "UTM10N",
    "32620": "UTM20N",
    "32618": "UTM18N",
    "32759": "UTM59S",
    "32720": "UTM20S",
    "32645": "UTM45N",
    "32650": "UTM50N",
    "32647": "UTM47N",
    "32722": "UTM22S",
    "32611": "UTM11N",
    "32651": "UTM51N",
    "32721": "UTM21S",
    "32653": "UTM53N",
    "32657": "UTM57N",
    "32608": "UTM08N",
    "32604": "UTM04N",
    "32758": "UTM58S",
    "32756": "UTM56S",
    "32655": "UTM55N",
    "32603": "UTM03N",
    "32605": "UTM05N",
    "4326": "Geographic WGS84",
    "900913": "Google Mercator",
    "0": "ORBIT"
}