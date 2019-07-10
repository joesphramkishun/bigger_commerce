CREATE TABLE Users (
  uid serial,
  bc_id text,
  email text,
  password_hash text,
  first_name text,
  last_name text,
  current_token text,
  cart_id text,
  about text,
  role text,
  address1 text,
  address2 text,
  phone text,
  city text,
  state_or_province text,
  state_or_province_code text,
  county_code text,
  postal_code text,
  billing_address1 text,
  billing_address2 text,
  billing_city text,
  billing_state text,
  billing_state_code text,
  billing_country_code text,
  billing_postal_code text,
  created_date timestamp default now(),
  gender text
);

CREATE TABLE Carts (
  id serial,
  bc_id text,
  uid integer,
  active boolean,
  order_id text,
  shipping_option_id text,
  consignment_id text,
  payment_token text,
  created_date timestamp default now()
);

CREATE TABLE Cookies (
  id serial,
  uid Integer,
  hash_token text,
  active boolean,
  created_date timestamp default now(),
  ip text
);
