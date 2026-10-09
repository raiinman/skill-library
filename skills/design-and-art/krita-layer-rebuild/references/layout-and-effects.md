# Layout, recoloring and effects

Read for posters, recurring graphic systems, palette variants, atmosphere or luminous/blur effects. All procedures are research adaptations pending native Krita verification. Use actual supported controls; imported Photoshop adjustments or brush tips do not establish equivalent native behavior.

## Reconstruct relationships across the composition

Record headline and body-text bounds, wording, line breaks, margins, alignments, image-to-text scale and repeated gap rhythms. Establish the dominant masses and grouping before ornament. Empty spaces can carry a design: letter counters, an arrow between letters, arches and the gaps between repeated marks depend on neighboring contours.

Construct recurring elements from a shared recipe but retain the promised independent instances. Preserve irregularities and functional distinctions—clock hands, labels and ticks should not become identical simply because they share a style. Compare at intended output size as well as enlarged views.

**Check:** changing one gap does not scale its neighboring glyphs; moving a text line does not move the illustration. A hole continues to reveal a changed background. Correct individual marks with incorrect group spacing still fail the composition.

Source: David Reinfurt, *A New Program for Graphic Design*, printed 36–41, 46–52, 99–116 (PDF 38–43, 48–54, 101–118). His accounts of Dürer, Thompson, Wertheimer and Bill are secondary evidence. Letter construction and fonts are in [text-and-fonts.md](text-and-fonts.md).

## Declare reuse semantics

Choose independent instances for separately editable objects; reserve linked instances for intentionally shared masters or derived effects. Record the source and destination identities, owned children, masks and dependency links. Copy the complete promised owner tree, then remap each dependency to the correct new or shared target. Clones follow a source and are unsuitable for independent painting. Preserve component ownership through delivery.

**Check:** change one duplicate's component and color while inspecting its original and siblings. Change a shared master and verify only declared linked instances update. Move the duplicate and check contacts, mapped details and newly exposed background. A duplicate layer name does not establish independent content.

Sources: Youngs, [object duplication](https://imagy.app/how-to-duplicate-or-copy-an-object-in-photoshop/); Adobe, [independent versus linked Smart Object copies](https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/duplicate-an-embedded-smart-object.html); Krita, [clone layers](https://docs.krita.org/en/reference_manual/layers_and_masks/clone_layers.html). Copy semantics must be checked in our actual native route.

## Separate tonal mapping from spatial coverage

A gradient map assigns colors according to input lightness. A spatial gradient changes across position. For split-colored light, retain both controls: form/value establishes the eligible planes; an object/region mask places the color and its strength. Inspect gradual transitions rather than copying an image-specific threshold. Keep atmosphere and sky/ground grading separately scoped when the reference requires different treatment.

For a palette variant, list material and lighting roles before recoloring. Similar lightness does not imply the same material; metal accents, skin and cloth can require exceptions. Preserve the faithful master, then compare the variant's form readability, edges and material distinctions. A hue rotation over the entire canvas is not evidence of independent object recoloring.

**Check:** change one light or garment color without altering unrelated objects. Toggle the mapping to inspect underlying value construction. Masks do not create missing facial planes. A transparency mask controls visibility, not protection against every edit; a filter mask and a global filter layer have different scopes.

Sources: *Adobe Photoshop Tricks and Tips*, edition 19, PDF 42–46, 68–79; Okku lessons 20 and 24. Screen has black as its neutral input; do not copy the book's incorrect generic 50%-gray explanation. Verify the intended blend visually and by actual layer scope.

For nearly black/white targets, adapt the owned tonal range along with pigment; hue-only changes can leave color invisible or folds flattened. Preserve the reference's relative fold values and separate material highlights. Compare comparable lit/shadow regions against the declared target color, then check isolated edges for contamination. Equal hue/saturation settings on different bases need not produce equal appearance. Clipped black/white contains no recoverable internal modeling; rebuilding absent detail is labeled inference.

Source: Smith, [black/white recoloring](https://photoshopcafe.com/photoshop-trick-turn-black-and-white-into-color/). Native tonal reconstruction is our adaptation to the source's retained photographic shading.

## Construct luminous objects with their consequences

Give each identified emitter or trail its own sharp/core geometry, wider halo and optional particulate marks. Separately own illumination falling on receiver surfaces, reflected accents and occlusion. Draw fire with an observed directional gesture and connected lobes; draw lightning with a main path and appropriate branches. Blur a derived halo, retaining an editable unblurred source.

**Check:** hiding the emitter also identifies which dependent receiver light should change. Moving a trail updates its halo, foreground crossings and surface lighting. Recoloring the core alone can leave an inconsistent halo. A glow must not erase essential silhouettes or conceal malformed geometry.

Sources: Leeuwe PDF 23–24; *Photoshop Tricks and Tips* PDF 46–49, 82–93; Okku lessons 19 and 28. Light source and received illumination are different owners with an explicit dependency.

Distinguish an inset luminous center from an exterior halo. Preserve the source geometry; derive the inset/halo with independently adjustable color, coverage and blur. Scale inset width to the narrowest intended strokes/counters, then verify they survive. A source-following clone with color/blur filter masks is a candidate Krita route; if unsupported, retain the master and explicitly regenerate owned effect marks after source edits. Reopen and edit the source again before claiming automatic propagation.

Sources: Sanchez, [editable glow](https://we.graphics/blog/how-to-create-an-editable-soft-glow-text-effect-in-illustrator) (inspected negative-offset figure creates an inset white region); Krita [clone-layer glow example](https://docs.krita.org/en/reference_manual/layers_and_masks/clone_layers.html). Application documentation does not validate our bridge route.

## Construct cast shadows on their receiver

Record caster silhouette/volume, light direction/extent and receiving planes. Own contact footprint, broader projected shape and local softness/strength separately where the target requires those controls. Reconstruct the shadow from these relationships after caster, light or receiver changes. A squashed silhouette is only an approximation for complex volume or uneven ground; inspect contact and local projection rather than accepting a global skew.

**Check:** reshape or move the caster, then inspect near/far edges, receiver clipping and exposed surface. Match observed softness and tone; uniform fading with distance is not a universal rule. Multiply affects compositing, not necessarily stored alpha, so inspect coverage separately from the dark appearance.

Source: Smith, [cast-shadow workflow](https://photoshopcafe.com/make-realistic-cast-shadow-photoshop-new-way/). Gradient and varying blur motivate separate controls; our dependency reconstruction remains untested.

## Build depth veils and transient particles

Place mist/smoke in front of or behind specific objects, with masks reflecting actual edge softness. Distinguish a hard solid occluder from a translucent veil. Snow/particle size, blur and contrast can indicate depth, but preserve the target distribution instead of inventing a more cinematic scene. If individual particles are promised editable, a flattened particle field is an unmet requirement.

**Check:** moving an object reveals a reconstructed continuation rather than a fixed background patch. Toggling a veil retains solid geometry. Nearby particles remain distinct from distant ones and do not move with an unrelated object. Contact shadows remain attached to their caster/receiver relationship, not to a fog sheet.

Sources: *Photoshop Tricks and Tips* PDF 34–41; Leeuwe PDF 25; Okku lessons 27–28.

## Make finish reversible and compare its effect

Keep an earlier checkpoint and unblurred geometry. Scope local blur, sharpened detail, color changes and lens/channel effects to their intended owners or derived preview. Retain editable masters if an effect requires a composite. Compare before/after in the same frame; accept only the effects that support the actual reference. A polished image with wrong contours or wording is still a fidelity failure.

**Check:** disable the effect without losing construction, inspect changed edges at native size, and compare the full image at output size. Reopen and verify the editing route before describing it as persistent. Source Photoshop parameters and imported presets are not universal Krita settings.

Sources: Okku lessons 19, 20 and 28; *Photoshop Tricks and Tips* PDF 56–61; Reinfurt printed 58–78 (PDF 60–80). Fast feedback improves the correction process, but does not prove improved matching.
