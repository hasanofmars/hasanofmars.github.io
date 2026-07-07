import { defineConfig } from "astro/config";

export default defineConfig({
  output: "static",
  server: {
    port: 4321,
  },
  build: {
    assets: "_assets",
  },
});
