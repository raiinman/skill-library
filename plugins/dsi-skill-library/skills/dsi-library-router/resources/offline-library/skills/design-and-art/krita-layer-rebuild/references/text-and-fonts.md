# Text, lettering and fonts

Read whenever text appears in a reference or the user requests new wording/reusable fonts.

## Select the deliverable

- Typeset text: retain literal Unicode wording, direction, font identity/uncertainty, layout and separate effects in actual editable text when supported. Prove wording replacement and size/spacing edits. Painted letters are a disclosed partial substitute, not a text pass.
- Custom lettering: retain semantic words separately from editable glyph/cluster contours, counters, joins, flourishes and effects. Shapes are the default. Changing wording may require drawing new letters and recomposing neighbors; mark absent glyphs inferred.
- Reusable font: deliver editable font source and a compiled font with declared repertoire, mapping, metrics and contextual behavior. Specify target scripts and sizes; a wordmark stored in a font cell or specimen picture does not establish typing support.

Resolve requested character coverage before calling a font reusable for new words. A declared subset serves only supported strings; an unspecified broad-font request remains incomplete until its repertoire is agreed and executed. Inspect a reproducible source/compiler/consumer route; if none is available, mark compilation tool-limited and continue independent illustration/letter-shape work.

## Construct and proof

Verify transcription before finish. For each word, record baseline or script-appropriate alignment, height, overall width, line breaks and neighbor gaps. For each glyph/cluster, mark extrema, junctions, terminals, stroke directions and counter boundaries. Construct skeleton/proportion first; then build inner and outer contours together so weight changes preserve the intended opening. Resolve joins before flourishes, outlines, shadows and distress. Keep those effects independently scoped.

Compare individual shapes, neighboring letters, full word and composition at intended size. A changed glyph can close a counter, change reading, collide with a descender or break a shared stroke. Repair those dependencies together. Script dots/diacritics are semantic content; measurement guides remain separate. Obtain informed script review when meaning is uncertain.

Straighten a faulty stem locally rather than scaling the word. Repair a curved bowl through extrema and tangent transitions rather than adding control points everywhere. Inspect terminals, joins and tight curves for kinks; automatic simplification can remove deliberate irregularity. Compare contour-to-contour white space as well as numeric advances: equal advances do not create equal apparent gaps. A whole-word compression cannot repair a distinctive wrong glyph.

**Checks:** move one crossbar while retaining its apex and counter; edit the gap between two letters without scaling either; hide the outline/shadow without losing the letter. Inspect small output sizes for closed counters and disappearing hairlines. For script lettering, compare initial, medial and terminal contexts where relevant; outlines that work in isolation can fail at joins.

Source: David Reinfurt, *A New Program for Graphic Design*, printed 22, 36–41, 46–52 and 79–96 (PDF 24, 38–43, 48–54 and 81–98). His accounts of Dürer, Thompson, Knuth and Dexter Sinister are secondary evidence. The geometric and parametric examples motivate landmarks and related controls; optical exceptions and script-specific construction remain necessary. These are proposed editing procedures, not a new tested font toolchain.

For reusable fonts, list observed and inferred glyphs. Record family relationships: height, width, weight, contrast, slant, terminals, roundness and counter treatment. Related parameters are starting constraints; inspect exceptional joins and curves rather than forcing every glyph through one formula. Keep editable contours, advance widths/bearings, character mapping, kerning and required substitution/attachment rules.

Proof representative straight/round/hybrid forms and controlled neighbor combinations, then unseen strings at two or more intended sizes. Use spacing strings such as `nsn` or `oso` only when those glyphs are in the declared repertoire; absent diagnostic characters remain a coverage gap. Check repertoire access, missing glyphs, spacing, counters, overlaps and contextual joins in the exported font. Reopen/edit source, rebuild and verify the changed output. Preserve errors/tool limits explicitly rather than substituting outline pictures.

Motivations: Hische's [lettering questions and decisions](https://jessicahische.is/aseriousoversharer) and Langdon's [ambigram construction](https://www.johnlangdon.net/thoughts/advice-on-ambigrams/) distinguish word-specific form relationships; Hoefler's [proofing guidance](https://jonathanhoefler.com/articles/how-to-proof-a-typeface) motivates controlled context tests; Frere-Jones's [design interview](https://type365.com/2016/10/19/design-angle-1-tobias-frere-jones/) motivates representative-form development rather than automatic font tooling. These are attributed research leads/motivations, not proof of a functioning implementation.

## Review logos and dimensional lettering

For logos or traced-letter candidates, review closed contours, counter holes, narrow gaps, shared boundaries and stray fragments with the reference hidden. Retain semantic parts independently. Inspect tangent transitions and editable handles at intended output size; detection or simplification supplies draft geometry, not accepted topology. Change one curve and recolor/move one part over another background, then save/reopen and repeat. Where editable handles cannot be retained, disclose that requirement rather than presenting sampled paint geometry as persistent vector editing.

Source: Sanchez, [logo tracing](https://we.graphics/blog/how-to-easily-trace-a-logo-in-photoshop/). Its final merge conflicts with per-part ownership; this adaptation retains authored native parts. Krita [vector-layer documentation](https://docs.krita.org/en/reference_manual/layers_and_masks/vector_layers.html) describes application editing, not a verified bridge creation route.

For dimensional lettering, retain semantic glyph/cluster masters, front/extrusion geometry, surface details and receiver reflections as separate editing roles. Transforming a container does not prove access to individual faces. A glyph/counter or extrusion edit must update its derived appearance; an independently edited surface mark must preserve glyph geometry. Inspect counter openness and face boundaries at output size, then reopen and repeat. A vertically flipped composite is a reflection approximation that can fail when view or receiver changes. Neither editable effects nor one constructed letter establishes reusable-font coverage.

Source: Vora, [3D textured text](https://www.photoshoptutorials.ws/photoshop-tutorials/text-effects/3d-textured-text-effect/), all four pages. Retained native roles and dependency updates are our adaptation to its cross-application Smart Object/texture workflow.

## Diagnose a failed word proof

Record outline/control changes separately from advances, pair spacing and full-layout changes. Repair a malformed contour/counter before expecting re-spacing to conceal it; when acceptable letters make an uneven word, inspect contour-to-contour white space and the actual connection. Connected-script overlap may be intended, while a self-crossing contour is a different topology question. A sampled intersection/containment check is bounded evidence, not complete curve validity or optical acceptance.

Log the affected glyph, contour, control/metric and reason; retain rejected proofs. Compare source-to-compiled contours, output-size words and terminal/medial contexts after repair. [Spiekermann and Carrois](https://www.myfonts.com/pages/fontshop-interview-with-erik-spiekermann-and-ralph-olivier-du-carrois-1) describe accountable revision comparisons; [Johnston’s spacing lesson](https://www.gutenberg.org/cache/epub/47089/pg47089-images.html) distinguishes apparent spaces; [Unger](https://www.eyemagazine.com/feature/article/reputations-gerard-unger) reports conversion/context failures. Physical manufacture and historical software accounts do not implement our toolchain.

Label authoring strings as diagnostics. For a genuine unseen-string check, freeze/hash the authored source before choosing new supported strings; do not count previously tuned strings as unseen. Test glyph/context coverage beyond compile success. A hand-drawn alternate does not establish GSUB/kerning/attachment support, and a seven-character working subset does not establish a complete family.

## Tool boundary

Inspect the selected connector's actual authoring/export actions. Krita's own [text tool](https://docs.krita.org/en/reference_manual/tools/text.html) has SVG text functionality, but UI/manual features and native API availability do not establish a callable bridge operation. Confirm text or font execution before promising it. If tooling is absent, preserve geometry/semantic planning and mark typing/font export tool-limited; continue independent reconstruction work. Installing a compiler or changing configuration requires authorization.
