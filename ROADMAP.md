# CNG Formats Guide — 2026 Roadmap

## Track 1: New Format Content + Decision Tree Development

### Task 1: Develop prerequisite content for decision framework

**Timeline: May - June 2026**

- General concepts section that includes chunking/partitioning, sharding, encoding, overviews. Link to those concepts from the formats they apply to rather than building out explanations for each individual file format. (Idea from [https://github.com/maxrjones](https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/30#issuecomment-2643053717))
- Zarr V3 deep dive: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/181
- Advanced COG topics: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/182
- GeoZarr explainer: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/110
- Updated HDF5 Guidance: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/180
- Virtual stores: VirtualZarr, Icechunk, Kerchunk update: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/173

### Task 2: Develop data format decision tree + framework

**July – August 2026**

- Create a format-selection flowchart (2D/3D cubes, vector, point clouds): https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/183
- Demonstrate framework in practice with a few examples and case studies

## Track 2: New Beyond the Format Content

**June - October**

### Task 1: Benchmarking Guidance

Intra-format benchmarking (e.g., Zarr chunking configurations) should happen within the format's documentation. Examples of inter-format comparisons could inform the decision framework. The decision framework could cite benchmark results but should not provide instructions on how to run benchmarks.

See also https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/30

### Task 2: Metadata section

- New Metadata Section: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/176
- Cross-format interoperability: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/184

## Track 3 — New Site Navigation Structure (parallel)

### Sitemap design
**Timeline: May - July (parallel with tracks 1 + 2)**

- Open new issue / discussion for sitemap options
- Intent-based nav (new data vs existing data)
- Engines & tooling section
- Get Stakeholder input

### New sitemap implementation
**August – October**

- Port existing content to new structure

## Track 4 — site redesign (optional)

### Visual redesign _(optional)_

**if capacity allows**

- New look and feel (Quarto theme or custom)
- Depends on sitemap being stable first
- User research to validate navigation patterns
