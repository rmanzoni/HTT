import os
import re 

from CMGTools.H2TauTau.officialJSONS import jsonMap

def lfnToDataset( lfn ):
    '''If lfn contains A/CMG/B, returns /B. Otherwise, returns lfn.'''
    pattern = re.compile( '.*/CMG(\S+)' )
    match = pattern.match( lfn )
    if match is not None:
        dataset = match.group(1)
        # print dataset
        return dataset
    return lfn

def jsonPick( dataset ):

    dataset = lfnToDataset(dataset)

    # stripping out the last part of the dataset name
    # to keep only the base official dataset name
    dsfields = dataset.lstrip('/').split('/')[0:3]
    # print dsfields
    baseDataSet = '/'+'/'.join( dsfields )
    jsonFile = jsonMap[ baseDataSet ]
    jsonAbsPath = jsonFile
    if not os.path.isfile(jsonAbsPath):
        raise ValueError( ' '.join([jsonAbsPath,
                                    'does not exist.']) )
    return jsonAbsPath

if __name__ == '__main__':

    samples = ['/Tau/Run2012A-13Jul2012-v1/AOD/V5_B/PAT_CMG_V5_14_0',
               '/Tau/Run2012A-recover-06Aug2012-v1/AOD/V5_B/PAT_CMG_V5_14_0',
               '/Tau/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_14_0',
               '/Tau/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_14_0',
               '/Tau/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_14_0',]

    #samples = ['/TauPlusX/Run2011A-May10ReReco-v1/AOD/foo/bar',
    #           '/TauPlusX/Run2011B-PromptReco-v1/AOD/blah',
    #           '/store/cmst3/user/cmgtools/CMG/TauPlusX/Run2011A-PromptReco-v4/AOD/V2/PAT_CMG_V2_4_0/tree_CMG_648.root',
    #           'should_fail_for_this_sample_name']

    for sample in samples:
        print 'Sample', sample
        print '\tJSON =', jsonPick( sample )


    
