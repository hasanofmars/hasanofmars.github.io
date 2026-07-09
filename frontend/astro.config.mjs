import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://hasanofmars.github.io",
  base: "/",
  output: "static",
  server: {
    port: 4321,
  },
});
