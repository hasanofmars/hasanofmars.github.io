import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import posts from '../data/blog.json';

export function GET(context: APIContext) {
  return rss({
    title: 'M Hasan - Blog',
    description: 'Thoughts on Linux, cybersecurity, and building secure systems.',
    site: context.site!,
    items: posts.map((post) => ({
      title: post.title,
      pubDate: new Date(post.date),
      description: post.excerpt,
      link: `/blog/${post.slug}/`,
    })),
    customData: '<language>en-us</language>',
  });
}
