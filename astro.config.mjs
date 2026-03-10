import { defineConfig } from 'astro/config';

export default defineConfig({
  outDir: './docs',
  build: {
    format: 'directory',
  },
});
