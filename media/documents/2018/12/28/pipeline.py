# Python Data Pipeline
import pandas as pd
import fastparquet
import medical_transform as mt
import medical_extract as me
import medical_schemas as schema

#TODO split output into another file
def saveOutputToParquet(df):
    dataSaved = False
    try:
    	# save output to parquet
    	df.to_parquet('df.parquet.gzip', compression='gzip')
    except:
    print "Unexpected error when saving to parquet:", sys.exc_info()[0]
        raise

#TODO split QA into another file
def checkNull(df,columnName, acceptableAmount):
    acceptableQuality = False
    nullPercent = df[columnName].isnull().sum()/df[columnName].count()
    if nullPercent >= acceptableAmount:
    	acceptableQuality = True
	return acceptableQuality

def main():
    # Extract
    medialclaims = me.extractData('fakemedicalclaims.csv', '|')
    metadata = me.extractData('fakemmetadata.csv', '|', 0 )

    # onfirm Extraction schema
    isMedicalSchemaValid = medialclaims.schema.validate(medicalInputSchema)

    # Apply business logic to transform data and merge in metadata
    if isMedicalSchemaValid:
    	transformedData = mt.transformMedicalData(medialclaims)
    	mergedData = mt.mergeMetadata(medialclaims, metadata)
	else:
		raise ValueError('The schema for medialclaims does not meet the required format')

    # Run QA checks to confirm data population
    isNameValid = checkNull(mergedData,'full_name',.9)
    isAgeValid = checkNull(mergedData,'age',.9)
    isGenderValid = checkNull(mergedData,'gender',1)

    #Run QA check to confirm output schema is correct
    isMedicalOutputSchemaValid = mergedData.validate(medicalOutputSchema)

    #TODO(scoyne): have this error identify the field causing the failure
    if not isNameValid || not isAgeValid || not isGenderValid || not isMedicalOutputSchemaValid:
        raise ValueError('The data quality for one or more columns does not meet the required threshold')
    else:
    # Save the output to parquet
    saveOutputToParquet(mergedData)

if __name__ == "__main__":
	main()