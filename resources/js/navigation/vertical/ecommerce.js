export default [
  { heading: 'Ecommerce' },
  {
    title: 'Products',
    icon: { icon: 'tabler-package' },
    children: [
      {
        title: 'All Products',
        to: 'apps-chat',
      },
      {
        title: 'Low qty Products',
        to: 'apps-chat',
      },
      {
        title: 'Create',
        to: 'apps-chat',
      },
    ],
  },
  {
    title: 'Categories',
    icon: { icon: 'tabler-category-2' },
    children: [
      {
        title: 'Categories',
        to: 'apps-chat',
      },
      {
        title: 'Subcategories',
        to: 'apps-chat',
      },
    ],
  },
  {
    title: 'Brands',
    icon: { icon: 'tabler-brand-alpine-js' },
    to: 'apps-calendar',
  },
  {
    title: 'Suppliers',
    icon: { icon: 'tabler-trolley' },
    to: 'apps-calendar',
  },
  {
    title: 'Payment',
    icon: { icon: 'tabler-credit-card' },
    to: 'apps-calendar',
  },
  {
    title: 'Currencies',
    icon: { icon: 'tabler-cash' },
    to: 'apps-calendar',
  },
  {
    title: 'Delivery',
    icon: { icon: 'tabler-truck' },
    to: 'apps-calendar',
  },
  {
    title: 'Locations',
    icon: { icon: 'tabler-current-location' },
    to: 'apps-calendar',
  },
]
