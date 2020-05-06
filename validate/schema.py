import sys
import numpy as np
from pandas_schema import Column
from pandas_schema.validation import MatchesPatternValidation, InRangeValidation, InListValidation, CustomSeriesValidation, CustomElementValidation, CanConvertValidation, IsDtypeValidation, CanCallValidation
#from validate.helpers import InInclusiveRangeValidation
from helpers import InInclusiveRangeValidation

#from validate.common_constants import *
from common_constants import *

STD_COLS_VAR = (EFFECT_DSET, CHR_DSET, BP_DSET, SNP_DSET) #OR_DSET, RANGE_L_DSET, RANGE_U_DSET, BETA_DSET, SE_DSET, FREQ_DSET , EFFECT_DSET, REF_DSET)
STD_COLS_VAR_POS = (EFFECT_DSET, CHR_DSET, BP_DSET)
STD_COLS_VAR_SNP = (EFFECT_DSET, SNP_DSET)

STD_COLS_EFFECT = (EFFECT_WEIGHT_DSET,OR_DSET,HR_DSET)

VALID_COLS = (EFFECT_WEIGHT_DSET, OR_DSET, HR_DSET, BETA_DSET, FREQ_DSET, LOCUS_DSET, EFFECT_DSET, REF_DSET, CHR_DSET, BP_DSET, SNP_DSET)

CURATOR_STD_MAP = {

    # variant id
    'rsID': SNP_DSET,
    # chromosome
    'chr_name': CHR_DSET,
    # base pair location
    'chr_position': BP_DSET,
    # odds ratio
    'OR': OR_DSET,
    # hazard ratio
    'HR': HR_DSET,
    # beta
    'beta': BETA_DSET,
    # effect allele
    'effect_allele': EFFECT_DSET,
    # reference allele
    'reference_allele': REF_DSET,
    # effect weight
    'effect_weight': EFFECT_WEIGHT_DSET
}

VALID_CHROMOSOMES = ['1', '2', '3', '4', '5', '6', '7', '8',
                     '9', '10', '11', '12', '13', '14', '15', '16',
                     '17', '18', '19', '20', '21', '22', '23', '24',
                     '25']

BUILD_MAP = {'28': 'NCBI28',
             '29': 'NCBI29',
             '30': 'NCBI30',
             '31': 'NCBI31',
             '33': 'NCBI33',
             '34': 'NCBI34',
             '35': 'NCBI35',
             '36': 'NCBI36',
             '37': 'GRCh37',
             '38': 'GRCh38'}

VALID_FILE_EXTENSIONS = [".txt", ".tsv", ".csv", ".tsv.gz", ".csv.gz", "gz", "gzip", ".tsv.gzip", ".csv.gzip"]

GENERIC_VALIDATORS = {
    SNP_DSET: Column(SNP_DSET, [CanConvertValidation(DSET_TYPES[SNP_DSET]), MatchesPatternValidation(r'^rs[0-9]+$')], allow_empty=True),
    CHR_DSET: Column(CHR_DSET, [InListValidation(VALID_CHROMOSOMES)], allow_empty=True),
    BP_DSET: Column(BP_DSET, [CanConvertValidation(DSET_TYPES[BP_DSET]), InInclusiveRangeValidation(1, 999999999)], allow_empty=True),
    EFFECT_WEIGHT_DSET: Column(EFFECT_WEIGHT_DSET, [CanConvertValidation(DSET_TYPES[EFFECT_WEIGHT_DSET])], allow_empty=True),
    OR_DSET: Column(OR_DSET, [CanConvertValidation(DSET_TYPES[OR_DSET])], allow_empty=True),
    HR_DSET: Column(HR_DSET, [CanConvertValidation(DSET_TYPES[HR_DSET])], allow_empty=True),
    BETA_DSET: Column(BETA_DSET, [CanConvertValidation(DSET_TYPES[BETA_DSET])], allow_empty=True),
    EFFECT_DSET: Column(EFFECT_DSET, [MatchesPatternValidation(r'^[ACTGNactgn]+$')], allow_empty=False),
    REF_DSET: Column(REF_DSET, [MatchesPatternValidation(r'^[ACTGNactgn]+$')], allow_empty=True),
    FREQ_DSET: Column(FREQ_DSET, [CanConvertValidation(DSET_TYPES[FREQ_DSET])], allow_empty=True),
    LOCUS_DSET: Column(LOCUS_DSET, [CanConvertValidation(DSET_TYPES[LOCUS_DSET])], allow_empty=True)
}

SNP_VALIDATORS = {k:v for k,v in GENERIC_VALIDATORS.items()}
SNP_VALIDATORS[SNP_DSET] = Column(SNP_DSET, [CanConvertValidation(DSET_TYPES[SNP_DSET]), MatchesPatternValidation(r'^rs[0-9]+$')], allow_empty=False)


POS_VALIDATORS = {k:v for k,v in GENERIC_VALIDATORS.items()}
POS_VALIDATORS[CHR_DSET] = Column(CHR_DSET, [InListValidation(VALID_CHROMOSOMES)], allow_empty=False)
POS_VALIDATORS[BP_DSET]  = Column(BP_DSET, [CanConvertValidation(DSET_TYPES[BP_DSET]), InInclusiveRangeValidation(1, 999999999)], allow_empty=False)

EFFECT_WEIGHT_VALIDATOR = {k:v for k,v in GENERIC_VALIDATORS.items()}
EFFECT_WEIGHT_VALIDATOR[EFFECT_WEIGHT_DSET] = Column(EFFECT_WEIGHT_DSET, [CanConvertValidation(DSET_TYPES[EFFECT_WEIGHT_DSET])], allow_empty=False)

OR_VALIDATOR = {k:v for k,v in GENERIC_VALIDATORS.items()}
OR_VALIDATOR[OR_DSET] = Column(OR_DSET, [CanConvertValidation(DSET_TYPES[OR_DSET])], allow_empty=False)

HR_VALIDATOR = {k:v for k,v in GENERIC_VALIDATORS.items()}
HR_VALIDATOR[HR_DSET] = Column(HR_DSET, [CanConvertValidation(DSET_TYPES[HR_DSET])], allow_empty=False)
