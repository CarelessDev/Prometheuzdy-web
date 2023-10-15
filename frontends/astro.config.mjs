import { defineConfig } from 'astro/config';

import react from "@astrojs/react";

// https://astro.build/config
export default defineConfig({
  output: 'static',
  outDir: '../app/static',
  base: 'static',
  integrations: [react()]
});