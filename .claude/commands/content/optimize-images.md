---
description: Optimize images for web performance and SEO
argument-hint: [directory-path] [--format webp|jpg|png] [--quality 85]
---

# Image Optimization

**Directory:** $1
**Format:** $2 (defaults to webp)
**Quality:** $3 (defaults to 85)

## Image Audit

### 1. Scan Directory

Analyze all images in $1:
- Total images found
- Current formats (jpg, png, gif, webp, svg)
- Total size before optimization
- Largest files that need attention

### 2. Optimization Strategy

**File Size Analysis:**
```
Current Status:
- Images over 1MB: [count]
- Images over 500KB: [count]
- Images over 100KB: [count]
- Total size: [X MB]

Target: All images under 100KB where possible
```

**Dimension Analysis:**
```
Oversized Images (need resizing):
- Images over 2000px wide: [list]
- Hero images (target: 1200x630): [list]
- Content images (target: 800px max): [list]
- Thumbnail images (target: 400px): [list]
```

### 3. Optimization Tasks

**For Each Image:**

1. **Resize Dimensions**
   - Hero/featured: 1200x630 (2x for retina: 2400x1260)
   - In-content: 800px max width
   - Thumbnails: 400px width
   - Icons: Keep as SVG or 64px/128px

2. **Format Conversion**
   - Photos: Convert to WebP (fallback: JPEG)
   - Graphics/logos: Keep as SVG or PNG (transparent)
   - Complex images: Progressive JPEG
   - Simple graphics: Consider SVG conversion

3. **Compression Settings**
   - WebP: Quality 85 for photos, 90 for graphics
   - JPEG: Quality 85, progressive encoding
   - PNG: Lossless compression, strip metadata
   - SVG: Minify and optimize paths

### 4. Implementation Commands

**Using ImageMagick (if available):**
```bash
# Batch convert to WebP
for img in *.{jpg,png}; do
  cwebp -q 85 "$img" -o "${img%.*}.webp"
done

# Resize large images
mogrify -resize '800>' *.jpg

# Strip metadata
mogrify -strip *.{jpg,png}
```

**Using Sharp (Node.js):**
```javascript
// Optimization script template
const sharp = require('sharp');
const fs = require('fs').promises;
const path = require('path');

async function optimizeImage(inputPath, outputPath) {
  await sharp(inputPath)
    .resize(800, null, {
      withoutEnlargement: true
    })
    .webp({ quality: 85 })
    .toFile(outputPath);
}
```

**Using Python Pillow:**
```python
from PIL import Image
import os

def optimize_image(input_path, output_path, max_width=800):
    img = Image.open(input_path)

    # Resize if needed
    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    # Save optimized
    img.save(output_path, 'WEBP', quality=85, method=6)
```

### 5. SEO Enhancement

**Filename Optimization:**
```
Before: IMG_20240315_123456.jpg
After:  blue-widget-product-showcase.webp

Pattern: [descriptor]-[keyword]-[context].ext
```

**Alt Text Generation:**
For each image, suggest descriptive alt text:
```
Image: hero-banner.jpg
Alt: "Blue widget product displayed on white background with measurement rulers"

Image: team-photo.jpg
Alt: "Development team collaborating at whiteboard during sprint planning meeting"
```

**File Structure:**
```
Recommended structure:
/images/
  /hero/          # Hero banners (1200x630)
  /content/       # In-post images (800px max)
  /thumbnails/    # List/grid thumbs (400px)
  /icons/         # SVG or small PNG
  /og/           # Open Graph images (1200x630)
```

### 6. Performance Metrics

**Before Optimization:**
- Total size: [X MB]
- Largest file: [filename, size]
- Average file size: [X KB]
- Page load impact: [estimated seconds]

**After Optimization:**
- Total size: [X MB] ([Y% reduction])
- Largest file: [filename, size]
- Average file size: [X KB]
- Page load improvement: [estimated seconds saved]

### 7. Responsive Images

**Generate HTML Picture Elements:**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg"
       alt="[descriptive alt text]"
       loading="lazy"
       width="800"
       height="450">
</picture>
```

**Srcset for Responsive:**
```html
<img srcset="image-400.jpg 400w,
             image-800.jpg 800w,
             image-1200.jpg 1200w"
     sizes="(max-width: 400px) 400px,
            (max-width: 800px) 800px,
            1200px"
     src="image-800.jpg"
     alt="[descriptive alt text]">
```

### 8. CDN & Caching

**Recommendations:**
- Enable browser caching: `Cache-Control: max-age=31536000`
- Use CDN for delivery (Cloudflare, CloudFront)
- Implement lazy loading for below-fold images
- Consider progressive enhancement

## Optimization Report

### ✅ Completed Tasks
- [ ] Resized [X] images to appropriate dimensions
- [ ] Converted [X] images to WebP format
- [ ] Reduced total size by [Y]%
- [ ] Added descriptive filenames
- [ ] Generated alt text for [X] images
- [ ] Created responsive versions

### 📊 Results Summary

**Performance Gains:**
- Page weight reduced: [X MB → Y MB]
- Est. load time saved: [X seconds]
- Bandwidth saved monthly: [estimated MB]

**SEO Improvements:**
- Images with alt text: [X/Y]
- Descriptive filenames: [X/Y]
- Proper dimensions: [X/Y]

### 🎯 Next Steps

1. Implement lazy loading for images
2. Set up automated optimization pipeline
3. Create image style guide for contributors
4. Monitor Core Web Vitals impact
5. Consider next-gen formats (AVIF)