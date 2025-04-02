# Business Loan Underwriting Schema

A comprehensive JSON Schema for business loan underwriting, designed for API ingestion and credit risk modeling. This schema incorporates industry-standard concepts from the Financial Industry Business Ontology (FIBO) while maintaining practical usability for fintech developers.

## Status

Current Version: 0.1.2
Status: Active Development

## Schema Location & Access

The schema is available at:
- Latest Version: [schema/business_loan_schema.v0.1.2.json](schema/business_loan_schema.v0.1.2.json)
- Canonical URI: `https://raw.githubusercontent.com/patterncg/business-loan-schema/v0.1.2/schema/business_loan_schema.v0.1.2.json`

Each version of the schema is tagged with its semantic version and can be accessed via the corresponding GitHub tag.

## Usage

### API Context
This schema is designed for use in business loan underwriting APIs, providing a standardized structure for:
- Loan application data collection
- Credit risk assessment
- Financial statement analysis
- Collateral evaluation
- Ownership structure documentation

### Validation
The schema follows JSON Schema draft-07 specification and can be validated using any standard JSON Schema validator. Example validation tools:
- [ajv-cli](https://github.com/jessedc/ajv-cli)
- [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema)

## Structure Overview

The schema consists of several key sections:

1. **Loan Details**
   - Core loan information
   - Purpose and terms
   - Collateral details

2. **Borrower Information**
   - Business entity details
   - Industry classification
   - Contact information

3. **Financial Statements**
   - Balance Sheet
   - Income Statement
   - Cash Flow Statement
   - Support for both historical and projected data

4. **Credit History**
   - Business credit scores
   - Payment behavior
   - Existing debts
   - Public records

5. **Ownership Structure**
   - Owner information
   - Ownership percentages
   - Personal guarantees

6. **External Factors**
   - Economic indicators
   - Industry benchmarks
   - Market conditions

## Versioning Strategy

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (MAJOR.MINOR.PATCH):

- **MAJOR** version changes indicate incompatible API changes
- **MINOR** version changes indicate backward-compatible functionality additions
- **PATCH** version changes indicate backward-compatible bug fixes

Each version is tagged in Git and the schema file is named accordingly (e.g., `business_loan_schema.v0.1.2.json`).

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
