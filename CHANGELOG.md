# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2025-03-31

### Added
- Application lifecycle tracking with new `applicationMetadata` section
- Structured financial statement data with specific formats for each statement type
- Support for projected financial statements with `isProjected` flag
- Standardized payment behavior summary at credit history level
- Comprehensive validation rules for numeric fields and identifiers

### Changed
- Refactored common address structure into reusable `$defs`
- Enhanced financial statement structure with required fields and categories
- Improved validation with minimum/maximum constraints and patterns
- Moved payment behavior summary from individual debts to credit history level
- Updated example document to reflect new schema structure

### Fixed
- Inconsistent financial statement data structure
- Missing validation for numeric fields
- Redundant address structure definitions
- Ambiguous payment behavior tracking

## [0.1.0] - 2025-03-31

### Added
- Initial JSON Schema for business loan underwriting
- Core schema structure with loanDetails, borrowerInformation, financialStatements, creditHistory, ownershipStructure, and externalFactors sections
- Comprehensive property descriptions and documentation
- Standard JSON Schema draft-07 validation rules
- Example JSON documents demonstrating schema usage

[unreleased]: https://github.com/tim/pattern/business-loan-schema/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/tim/pattern/business-loan-schema/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/tim/pattern/business-loan-schema/releases/tag/v0.1.0 