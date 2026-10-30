# Deployment and local development

## Static preview

Run `python3 src/build.py`, then serve `dist/` with a static server. The build clears and recreates only its own output directory. Python's standard library is sufficient.

For a hosted preview, publish the contents of `dist/` at the origin root. Root-relative routes and asset URLs assume this location. A GitHub Pages *project subpath* such as `/TheHACStudios/` requires a base-path adaptation; simply uploading this build there would break navigation and assets. The repository instead links the existing live website at https://www.thehacstudios.com/.

Before a production static deployment:

- Set `CANONICAL_DOMAIN` in `src/build.py` to the intended domain.
- Confirm captions, social links, pricing, and contact details.
- Connect and validate an actual inquiry backend if needed; the repository form is a demonstration.
- Rebuild and verify every generated page, image, stylesheet, and video.
- Use HTTPS and a static host capable of serving directory `index.html` files and MP4 content.

## WordPress customizations

1. Create a WordPress installation with your own database and administrator credentials.
2. Install the Esthetic parent theme and required Gutenverse dependencies from their authorized distribution.
3. Copy `wordpress/esthetic-child` to `wp-content/themes/esthetic-child`.
4. Activate the child theme and configure permalinks.
5. Create/import your own pages and approved media; the production database is not included.
6. Update the featured-film upload path in `functions.php` if your asset uses a different location.
7. Verify home, stories, legacy redirects, social icons, and film playback on the target domain.

The child theme alone does not recreate all production pages. No credentials or hosting settings from the original deployment are needed or provided.

## Troubleshooting

| Symptom | Check |
|---|---|
| Static pages are unstyled | Serve `dist/` at the origin root, then rebuild |
| Broken image | Check the media-selection path against `src/assets/` |
| Video does not autoplay | Browsers may block autoplay; use the poster or play control |
| Custom WordPress styles missing | Parent theme must be installed and child theme active |
| WordPress film missing | Upload media and adjust the film path in `functions.php` |
| Inquiry does not arrive | The static form is a demo; no message transport is configured |
