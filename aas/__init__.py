"""
The package consists of the python implementation of the AssetAdministrationShell, as defined in the
'Details of the Asset Administration Shell' specification of Plattform Industrie 4.0.

The subpackage 'model' is an implementation of the meta-model of the AAS,
in 'adapter', you can find JSON and XML adapters to translate between PyI40AAS objects and JSON/XML schemas;
and in 'util', some helpful functionality to actually use the AAS meta-model you created with 'model' is located.
"""
import warnings

warnings.warn("PyI40AAS is deprecated. Please use Eclipse BaSyx Python instead.", DeprecationWarning, stacklevel=2)
