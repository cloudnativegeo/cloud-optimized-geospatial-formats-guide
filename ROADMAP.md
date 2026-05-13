# CNG Formats Guide — 2026 Roadmap

The timelines below are _proposed_ based of a logical sequence of development. Any given task may be picked up sooner or later depending on interest, availability and demand.

## Track 1 (T1): New or Updated Content on Formats + Decision Tree Development

### T1 Task 1: Develop prerequisite content for decision framework

**Timeline: May - June 2026**

- General concepts section: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/195
- Zarr V3 deep dive: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/181
- Advanced COG topics: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/182
- GeoZarr explainer: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/110
- Updated HDF5 Guidance: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/180
- Virtual stores: VirtualZarr, Icechunk, Kerchunk update: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/173

### T1 Task 2: Develop data format decision tree + framework

**July – August 2026**

- Create a format-selection flowchart (2D/3D cubes, vector, point clouds): https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/183
- Demonstrate framework in practice with a few examples and case studies

## Track 2 (T2): New Non-Format Content 

### T2 Task 1: Performance Fundamentals + Benchmarking Guidance

**September - October 2026**

Provide guidance on performance and benchmarking. This will require some thought. Some existing considerations:

1. Intra-format benchmarking (e.g., Zarr chunking configurations) should happen within the format's documentation.
2. Examples of inter-format comparisons could inform the decision framework. The decision framework could cite benchmark results but should not provide instructions on how to run benchmarks.
3. https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/191
4. https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/30

### T2 Task 2: Metadata section

**September - October 2026**

- Add a metadata section: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/176
- Cross-format interoperability: https://github.com/cloudnativegeo/cloud-optimized-geospatial-formats-guide/issues/184

## Track 3 (T3) — New Site Navigation Structure (parallel track)

Users of the site could benefit from a modified site navigation. This new structure could be designed and implemented in parallel with the content tracks.

### T3 Task 1: Sitemap design

**Timeline: May - July 2026 (parallel with tracks 1 + 2)**

- Open new issue / discussion for sitemap options
- Gather stakeholder input to validate potential navigation patterns
- Consider intent-based nav (new data vs existing data). Engines & tooling section.
- Design new structure

### T3 Task 2: New sitemap implementation

**August – October 2026**

- Port existing content to new structure

## Track 4 (T4) — Site Redesign (optional)

### Visual redesign _(optional)_

If capacity allows, develop new look and feel (Quarto theme or custom).
